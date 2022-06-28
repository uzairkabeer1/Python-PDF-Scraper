import pdfquery

pdf = pdfquery.PDFQuery('BUSTA_PAGA - 2.pdf')
pdf.load()
pdf.tree.write('pdfXML.txt', pretty_print = True)

Name = pdf.pq('LTTextLineHorizontal:overlaps_bbox("25.509, 729.284, 102.06, 737.284")').text()
Nam = pdf.pq('LTTextLineHorizontal:overlaps_bbox("25.509, 740.621, 97.031, 748.621")').text()

N = pdf.pq('LTTextLineHorizontal:overlaps_bbox("25.509, 706.61, 188.558, 714.61")').text()

A = pdf.pq('LTTextLineHorizontal:overlaps_bbox("425.166, 668.04, 570.398, 676.04")').text()
B = pdf.pq('LTTextLineHorizontal:overlaps_bbox("538.588, 479.073, 569.716, 515.873")').text()

print(Name,'\n',Nam,'\n',N,'\n',A,'\n',"Competenze:",B)
