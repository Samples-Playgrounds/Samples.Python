from context_compressor import ContextCompressor

# Initialize the compressor
compressor = ContextCompressor()

# Compress text
text = """
Artificial Intelligence (AI) is a broad field of computer science focused on 
creating systems that can perform tasks that typically require human intelligence. 
These tasks include learning, reasoning, problem-solving, perception, and language 
understanding. AI has applications in various domains including healthcare, finance, 
transportation, and entertainment. Machine learning, a subset of AI, enables 
computers to learn and improve from experience without being explicitly programmed.
"""

result = compressor.compress(text, target_ratio=0.5)

print("Original text:")
print(text)
print(f"\nCompressed text ({result.actual_ratio:.1%} of original):")
print(result.compressed_text)
print(f"\nTokens saved: {result.tokens_saved}")
print(f"Quality score: {result.quality_metrics.overall_score:.2f}")

