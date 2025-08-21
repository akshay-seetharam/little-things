class TierList:
    def __init__(self, tierdict):
        self.tierdict = tierdict
    def __str__(self):
        for i, val in enumerate(sorted(list(tierdict.keys()))):
            print(f'{val}: {tierdict[i]}')

    def merge(tierlists):
         items = list(tierlists[0].values())
         tiers = {}
         for i in items:
            tiers_i = TierList.find(tierlists, i)
            avg_tier = TierList.average_tier(tiers_i)
            tiers[avg_tier] = i if avg_tier not in tiers else tiers[avg_tier].append(i)
         return tiers

    def average_tier(tiers_i):
        numified = [ord(_) for _ in tiers_i]
        minimum = min(numified) if numified is not [] else return 5
        j = 0
        while j < len(tiers_i):
            numified[j] = numified[j] - minimum
            j += 1
        return sum(numified)/len(numified)

    def find(tierlists, i):
        tiers = []
        for tl in tierlists:
            for j in list(tl.keys()):
                if i in tl[j]:
                    tiers.append(j)
                    continue
        return tiers

if __name__ == '__main__':
    num = int(input('How many tier lists?\n').strip())
    tls = []
    for i in range(num):
        tier = input('What tier?\n').strip()
        tierdict = {tier: []}
        decision = input('blank if done; val if not done with tier?\n').strip()
        while len(decision) > 0:
             tierdict[tier] = decision
        
