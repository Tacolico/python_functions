first_page=1
end_page=19
white_page=20
bundle=10
book_total=abs(first_page-end_page)/4/bundle
bun_page=4*bundle
last_bundle=1+int(book_total%1*bundle)
last_bun_bundle=4*last_bundle
book_total=int(book_total)

print(f"Prepare {bundle} pages")
def page_list(first_page,last_page,pages,end_page,white_page):
    first_print=[]
    seccond_print=[]
    to_print=[i for i in range(first_page,last_page,1)]
    for j in range(pages):
        left_page=to_print[-1]-2*j
        right_page=to_print[0]+2*j
        if left_page > end_page:
            left_page=white_page
        if right_page > end_page:
            right_page=white_page
        first_print.append(left_page)
        first_print.append(right_page)
        if j == pages-1:
            continue
    for j in range(pages-1,-1,-1):
        left_page=to_print[0]+1+2*j
        right_page=to_print[-1]-1-2*j
        if left_page > end_page:
            left_page=white_page
        if right_page > end_page:
            right_page=white_page
        seccond_print.append(left_page)
        seccond_print.append(right_page)
        if j == 0:
            continue
    print(first_print)
    print(seccond_print)
  
for i in range(book_total):
    print(f"Bundle {i+1}:")
    begin=first_page+bun_page*i
    end=first_page+bun_page*(i+1)
    page_list(begin,end,bundle,end_page,white_page)
    print("")
print(f"Prepare {last_bundle} pages")
if i == None:
    i=0
print(f"Bundle {i+2}:")
begin=first_page+bun_page*(i+1)
end=first_page+bun_page*(i+1)+last_bun_bundle
page_list(begin,end,last_bundle,end_page,white_page)
