def printer_queue(doc_count, doc_index, docs):
    doc_check = ["True" if i == doc_index else "False" for i in range(len(docs))]
    count = 0

    while True:
        if docs[0] == max(docs):
            count += 1

            if doc_check[0] == "True":
                return count

            docs.remove(docs[0])
            doc_check.remove(doc_check[0])
        else:
            temp_num = docs[0]
            temp_check = doc_check[0]

            docs.remove(docs[0])
            doc_check.remove(doc_check[0])

            docs.append(temp_num)
            doc_check.append(temp_check)


def main():
    num = int(input())

    for _ in range(num):
        doc_count, doc_index = map(int, input().split())
        docs = list(map(int, input().split()))

        print(printer_queue(doc_count, doc_index, docs))


if __name__ == "__main__":
    main()
