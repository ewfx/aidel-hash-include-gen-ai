from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


class Summarizer:
    def __init__(self, model_name) -> None:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.summarizer = pipeline(
            "summarization", model=model, tokenizer=tokenizer)

    # Summarize text with better handling of large inputs
    def summarize_text(self, text, max_length=500, chunk_size=2000):
        # Split into manageable chunks
        chunks = [text[i:i + chunk_size]
                  for i in range(0, len(text), chunk_size)]

        # Summarize each chunk
        summaries = []
        for chunk in chunks:
            summary = self.summarizer(
                chunk, max_length=max_length, min_length=50, do_sample=False)[0]['summary_text']
            summaries.append(summary)

        # Combine all chunk summaries
        combined_summary = " ".join(summaries)

        # Optional: Hierarchical summarization to refine final summary
        if len(combined_summary) > 2000:  # Chunk limit
            combined_summary = self.summarizer(
                combined_summary, max_length=max_length, min_length=50, do_sample=False)[0]['summary_text']

        return combined_summary
