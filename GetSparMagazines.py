from PaperBoi.Providers.SparProvider import SparProvider


spar_provider = SparProvider()

for magazine in spar_provider.DownloadMagazines():
    print(magazine)
