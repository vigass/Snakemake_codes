rule all:
    input:
        "volcano.tiff"

rule generate_volcano_plot:
    input:
        script="volcanoplot.py",
        data="result.csv"
    output:
        "volcano.tiff"
    conda:
         "environment.yaml"
    shell:
         """
	python {input.script} --input {input.data} --output {output} 
	 """
