def analyze_document(text: str) -> str:
    """
    Simple financial text analyzer.
    - Detects revenue, profit, growth
    - Summarizes into plain English
    """

    summary = []

    if "revenue" in text.lower():
        summary.append("Mentions revenue figures.")
    if "profit" in text.lower():
        summary.append("Mentions profit.")
    if "growth" in text.lower() or "%" in text:
        summary.append("Mentions growth or percentages.")

    if not summary:
        summary.append("General financial text without key metrics.")

    return " ".join(summary)
