# DATA-SCRAPER

So the steps involved in data scraping from this website are:
1. We have to use both selenium and beautifulsoup as it is a dynamically loaded website.
2. We then go to the website and locate the view details button.
3. Then we locate the different elements under the project overiew and promoter details.
4. We then iterate the script in order to fetch the first 6 projects.
5. We give significatant load time for all elements to load.
6. I had faced the issue of stale elements, so I had to also iterate the locating of view details.
7. After this the data is stored as a list.

The data is stored in the format of ['Project name', 'Rera no', 'Promoter name', 'Address', 'GST']

The output obtained: [['Basanti Enclave', 'RP/01/2025/01362', 'M/S. NEELACHAL INFRA DEVELOPERS PVT. LTD', 'Gurudwara, PO-South Balanda, Via: Talcher Rural INR, Angul-759116, Dist. Angul, Odisha ,,,,,', '21AADCN5439J2ZH'], ['UDYAYEEN', 'RP/19/2025/01361', 'SHYAMCHAND BUILDERS PRIVATE LIMITED', 'MIG-II 21/2 Ground Floor,Chandrasekharpur,Bhubaneswar,Khordha,Odisha,751016', '21ABCCS4755J1ZB'], ['BARSANA RESIDENCY - II', 'PS/28/2025/01360', 'Propietory NameRITA PODDAR', 'Current Residence AddressPLOT NO-2570,PODDAR HEIGHTS,PODDAR COLONY,KHETRAJPUR,Sambalpur,Odisha,768003', '21AREPP3171E1Z7'], ['KRISHNA MANOR PH-II', 'PS/7/2025/01358', 'KRISHNA PROPERTIES & DEVELOPERS PRIVATE LIMITED', 'Plot No-46, Indraprastha Housing Colony, Phase-II, Pokhariput, Bhubaneswar, Khordha, Odisha-751020.,,,,,', '21AAECK8663L2Z7'],['BHAVYAVILLA', 'PS/19/2025/01351', 'SUNSHINE INFRATECH', 'PLOT NO 339,GOUTAMNAGAR,BJB NAGAR,Khordha,Odisha,751014', '21ACMFS3976P1ZC'], ['MURALIDHARA HEIGHTS', 'RP/19/2025/01355', 'TRILOCHAN PROJECTS AND DEVELOPERS PVT. LTD', 'Plot No-208, Flat No-301,Trilochan Plaza,Saheed Nagar,Bhubaneswer,Khordha,Odisha,751007', '21AAGCT0547E1ZT']]
