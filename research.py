from ddgs import DDGS

def research_company(company_name):

    with DDGS() as ddgs:
        results = ddgs.text(company_name, max_results=3)

        info = []
        for r in results:
            info.append(r["body"])

    summary = " ".join(info)

    data = {
        "name": company_name,
        "research": summary
    }

    return data