# import pydeseq2 as de
# import pandas as pd
# import argparse

# def runDeseq(countsTable, colData):
#     colData['Treat'] = pd.Categorical(colData['Treat'], categories=['T0', 'treatment', 'control'])
#     colData = pyDESeq2.sample_metadata(colData)

#     ### Create DESeq Object
#     dds = pyDESeq2.DESeqDataSetFromMatrix(
#         countData=countsTable,
#         colData=colData,
#         design='~ 0 + Treat'
#     )

#     ### Normalize counts
#     dds = pyDESeq2.DESeq(dds, test="LRT", reduced='~ 1')

#     ## print DESeq tests result names
#     print(dds.resNames)

#     return dds

# def writeResult(res,resName):
#     res.to_csv(resName, sep="\t", quote=FALSE, index=True, header=True)

# def getResult(
#     dds, numerator, denominator, sgRNA2gene, cond='Treat', write=False, name=None
# ):
#     res = pyDESeq2.results(
#         dds,
#         contrast=[f"{cond}{numerator}", f"{cond}{denominator}"],
#         listValues=[1, -1]
#     )

#     res = pd.concat([sgRNA2gene, res], axis=1)

#     if(write):
#         writeResult(
#             res,
#             f"{name}R{numerator}_vs_{denominator}.txt"
#         )
#     else:
#         return res

# def getPheScores(dds, Treatment, Control, sgRNA2gene, T0):
#     ## rho  – treatment vs ctrl
#     getResult(dds, Treatment, Control, sgRNA2gene, write=True, name='rho')

#     ## gamma  – ctrl vs T0
#     if (T0):
#         getResult(dds, Control, T0, sgRNA2gene, write=True, name='gamma')

#     ## tau  – treatment vs T0
#     if (T0):
#         getResult(dds, Treatment, T0, sgRNA2gene, write=True, name='tau')

#     ## kappa  – combination treatment vs. single treatment
#     # not implemented

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Run DESeq2 analysis.')
#     parser.add_argument('-i', '--counts', type=str, required=True, help='Path to counts table.')
#     parser.add_argument('-s', '--samplesheet', type=str, required=True, help='Path to sample sheet.')
#     parser.add_argument('-t', '--treatment', type=str, required=True, help='Name of samples in treatment condition.')
#     parser.add_argument('-c', '--control', type=str, required=True, help='Name of samples in control condition.')
#     parser.add_argument('-z', '--T0', type=str, default=None, help='Name of samples in T0 condition.')

#     args = parser.parse_args()

#     print('Load count matrix and samplesheet!')
#     RawTable = pd.read_table(args.counts, index_col=0)
#     sgRNA2gene = RawTable['target'].to_frame()
#     countsTable = RawTable.drop(columns='target')

#     colData = pd.read_csv(args.samplesheet, index_col='Index')

#     print('Run test!')
#     dds = runDeseq(countsTable, colData)

#     print('Extract Normalized counts!')
#     normalized_counts = dds.normalizedCounts()
#     writeResult(normalized_counts, args.counts.replace('.txt', '_DESeq2_normalized.txt'))

#     print('Extract results!')
#     getP
