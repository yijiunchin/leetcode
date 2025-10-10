class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy.reverse()
        answers = []
        for i in range(len(energy)):
            if i < k: answers.append(energy[i])
            else: answers.append(energy[i] + answers[i - k])
        return max(answers)

