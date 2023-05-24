mkdir -p logs/
mkdir -p logs/trim/
mkdir -p fastq/trim/


for f in fastq/*_R1.fastq.gz; do 
    b=`basename $f`
    sample=${b/_R1.fastq.gz}
    
    echo $sample
    fq1out=fastq/trim/${sample}_R1.fastq;
    fq2out=fastq/trim/${sample}_R2.fastq;
    fq1in=fastq/${sample}_R1.fastq.gz;
    fq2in=fastq/${sample}_R2.fastq.gz;

    # https://cutadapt.readthedocs.io/en/stable/guide.html
    # cutadapt -j 30 -q 10 --action=retain \
    #     -a NNNNNNNNNNNNNNNNNNNNNNNNNNNNN \
    #     -A NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN \
    #     -o fastq/trim/${sample}_R1.fastq.gz -p fastq/trim/${sample}_R2.fastq.gz \
    #     fastq/${sample}_R1.fastq.gz fastq/${sample}_R2.fastq.gz &> logs/trim/${sample}_trim.log
    # gzip -dc ${fq1in}.gz > ${fq1in}
    
    ##Tom: trim reads 1-29 bases (R1 doesn't seq first G) or 1-30 (R2 sequences full protospacer)
    zcat $fq1in | fastx_trimmer -v -f 1 -l 29 -i - -o $fq1out &> logs/trim/${sample}_trim.log;
    zcat $fq2in | fastx_trimmer -v -f 1 -l 30 -i - -o $fq2out &>> logs/trim/${sample}_trim.log;
    gzip $fq1out;
    gzip $fq2out;
done
