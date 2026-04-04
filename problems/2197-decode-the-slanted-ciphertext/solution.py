class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        return "".join(
            encodedText[r * cols + c + r]
            for c in range(cols)
            for r in range(rows)
            if c + r < cols
        ).rstrip()
