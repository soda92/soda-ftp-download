# %%
def is_jupyter():
    try:
        __IPYTHON__ # type: ignore
        return True
    except NameError:
        return False
is_jupyter()

# %%
from soda_ftp_download import download_file  # noqa: E402

download_file("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/000/SRR1810900/SRR1810900.fastq.gz")

# %%
