import pandas as pd
class ReadandWrite:
    def read():
        df = pd.read_excel("Excel/Data_assess.xlsx", usecols=['Name', 'SkillSet', 'Experience'])
        return df.values[:,:].tolist()

ans = ReadandWrite.read()
print(ans)