## DDRi collab AZ-IGI (UCSF)

Sample name format:

```
<study_model>__<platform>__<perturbation>__<replicate>
```

Files map:

```
.
├── 1-evaluate-DDRi-v2-screens.ipynb
├── 2-drug-gene-knowledge-graph.ipynb
├── 3-evaluate-DDRi-PRDX1-v3-screens.ipynb
├── LICENSE
├── README.md
└── screens
    ├── A549_CRISPRa_v2_screen_analysis.ipynb
    ├── A549_CRISPRa_v2_screens.h5ad.gz
    ├── A549_CRISPRa_v2_screens.pkl
    ├── A549_CRISPRi_v2_screen_analysis.ipynb
    ├── A549_CRISPRi_v2_screens.h5ad.gz
    ├── A549_CRISPRi_v2_screens.pkl
    ├── A549_PRDX1_CRISPRi_v3.h5ad.gz
    ├── A549_PRDX1_CRISPRi_v3_samplesheet.txt
    ├── A549_PRDX1_CRISPRi_v3_screen_analysis.ipynb
    ├── A549_PRDX1_CRISPRi_v3_screens.pkl
    ├── CRISPRa_v2_human_librarytable.txt.gz
    ├── CRISPRi_v2_human_librarytable.txt.gz
    ├── CRISPRi_v3_human_librarytable.txt.gz
    └── fastq
        ├── A549__CRISPRa_v2__DMSO__rep1.fastq.gz
        ├── A549__CRISPRa_v2__Pi__rep1.fastq.gz
        ├── A549__CRISPRa_v2__PiRi__rep1.fastq.gz
        ├── A549__CRISPRa_v2__PiWi__rep1.fastq.gz
        ├── A549__CRISPRa_v2__Ri__rep1.fastq.gz
        ├── A549__CRISPRa_v2__T0__rep1.fastq.gz
        ├── A549__CRISPRa_v2__Wi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__DMSO__rep1.fastq.gz
        ├── A549__CRISPRi_v2__DMSO__rep2.fastq.gz
        ├── A549__CRISPRi_v2__Ki__rep1.fastq.gz
        ├── A549__CRISPRi_v2__Ki__rep2.fastq.gz
        ├── A549__CRISPRi_v2__Mi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__Mi__rep2.fastq.gz
        ├── A549__CRISPRi_v2__PiKi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__PiKi__rep2.fastq.gz
        ├── A549__CRISPRi_v2__PiMi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__PiMi__rep2.fastq.gz
        ├── A549__CRISPRi_v2__Pi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__Pi__rep2.fastq.gz
        ├── A549__CRISPRi_v2__PiRi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__PiRi__rep2.fastq.gz
        ├── A549__CRISPRi_v2__PiWi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__PiWi__rep2.fastq.gz
        ├── A549__CRISPRi_v2__Ri__rep1.fastq.gz
        ├── A549__CRISPRi_v2__Ri__rep2.fastq.gz
        ├── A549__CRISPRi_v2__T0__rep1.fastq.gz
        ├── A549__CRISPRi_v2__T0__rep2.fastq.gz
        ├── A549__CRISPRi_v2__Wi__rep1.fastq.gz
        ├── A549__CRISPRi_v2__Wi__rep2.fastq.gz
        ├── A549_parent__CRISPRi_v3__DNAPKi__rep1_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__DNAPKi__rep1_R2.fastq.gz
        ├── A549_parent__CRISPRi_v3__DNAPKi__rep2_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__DNAPKi__rep2_R2.fastq.gz
        ├── A549_parent__CRISPRi_v3__DNAPKi__rep3_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__DNAPKi__rep3_R2.fastq.gz
        ├── A549_parent__CRISPRi_v3__T0__rep1_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__T0__rep1_R2.fastq.gz
        ├── A549_parent__CRISPRi_v3__T0__rep2_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__T0__rep2_R2.fastq.gz
        ├── A549_parent__CRISPRi_v3__vehicle__rep1_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__vehicle__rep1_R2.fastq.gz
        ├── A549_parent__CRISPRi_v3__vehicle__rep2_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__vehicle__rep2_R2.fastq.gz
        ├── A549_parent__CRISPRi_v3__vehicle__rep3_R1.fastq.gz
        ├── A549_parent__CRISPRi_v3__vehicle__rep3_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__DNAPKi__rep1_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__DNAPKi__rep1_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__DNAPKi__rep2_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__DNAPKi__rep2_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__DNAPKi__rep3_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__DNAPKi__rep3_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__T0__rep1_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__T0__rep1_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__T0__rep2_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__T0__rep2_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__vehicle__rep1_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__vehicle__rep1_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__vehicle__rep2_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__vehicle__rep2_R2.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__vehicle__rep3_R1.fastq.gz
        ├── A549_PRDX1KO__CRISPRi_v3__vehicle__rep3_R2.fastq.gz
        └── checksums.txt

```