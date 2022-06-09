from datetime import date


class CPRDayBean:
    Pivot = 0
    bc = 0
    tc = 0
    R1 = 0
    S1 = 0
    R2 = 0
    S2 = 0
    R3 = 0
    S3 = 0
    R4 = 0
    S4 = 0
    cpr_date = date(2020, 6, 10)

    def __init__(self):
        self.Pivot = 0
        self.bc = 0
        self.tc = 0
        self.R1 = 0
        self.S1 = 0
        self.R2 = 0
        self.S2 = 0
        self.R3 = 0
        self.S3 = 0
        self.R4 = 0
        self.S4 = 0
        self.cpr_date = date(2020, 6, 10)


    def calculateCPR(self, row):
        self.Pivot = (row.High + row.Low + row.Close) / 3
        self.BC = (row.High + row.Low) / 2
        self.TC = (self.Pivot - self.BC) + self.Pivot

        self.R1 = 2 * self.Pivot - row.Low
        self.R2 = self.Pivot + (row.High - row.Low)
        self.R3 = self.R1 + (row.High - row.Low)
        self.R4 = self.R3 + (self.R2 - self.R1)

        self.S1 = 2 * self.Pivot - row.High
        self.S2 = self.Pivot - (row.High - row.Low)
        self.S3 = self.S1 - (row.High - row.Low)
        self.S4 = self.S3 - (self.S1 - self.S2)


    def calculateCPR_input_values(self, high, low, close):
        self.Pivot = (high + low + close) / 3
        self.BC = (high + low) / 2
        self.TC = (self.Pivot - self.BC) + self.Pivot
        self.R1 = 2 * self.Pivot - low
        self.R2 = self.Pivot + (high - low)
        self.R3 = self.R1 + (high - low)
        self.R4 = self.R3 + (self.R2 - self.R1)

        self.S1 = 2 * self.Pivot - high
        self.S2 = self.Pivot - (high - low)
        self.S3 = self.S1 - (high - low)
        self.S4 = self.S3 - (self.S1 - self.S2)
