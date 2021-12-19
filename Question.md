# Assignment Question

You are given a dataset in CSV format (see [`File_A.txt`](File_A.txt)). A preview of the dataset is as below:

GO id|contig
-|-
GO:0000009|vpl_contig_18129
GO:0000023|vpl_contig_35089
GO:0000023|vpl_contig_53542
GO:0000045|vpl_contig_69103
GO:0000062|vpl_contig_45471


# Instruction

Write a Python code that:

1. Read the input file in CSV format ([`File_A.txt`](File_A.txt))
2. Group the contig according to the GO id and keep it in CSV format with a tab as the delimiter
3. Write the output in another CSV file

**Note**: a tab shall be used as the delimiter instead of a comma (,)  


# Expected Output

Below is a preview of the expected output from your python script:

GO id|contig
-|-
GO:0000009|vpl_contig_18129        
GO:0000023|vpl_contig_35089 vpl_contig_53542        
GO:0000045|vpl_contig_69103        
GO:0000062|vpl_contig_45471        
GO:0000064|vpl_contig_25360        
GO:0000070|vpl_contig_34176        
GO:0000096|vpl_contig_13588 vpl_contig_486 vpl_contig_6418 vpl_contig_6479

You can see [`File_O.txt`](File_O.txt) as an example.
