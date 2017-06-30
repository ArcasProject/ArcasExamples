import arcas
import pandas as pd

keywords = ["sustainable software", "research software"]
num_collect = 10
max_num = 31

dfs = []
for p in [arcas.Nature, arcas.Arxiv, arcas.Ieee, arcas.Plos, arcas.Springer]:
    api = p()
    for key in keywords:
        start = 1
        switch = True
        while start < max_num and switch is True:
            parameters = api.parameters_fix(title=key, records=num_collect,
                                            abstract=key, start=start)

            url = api.create_url_search(parameters)

            request = api.make_request(url)
            root = api.get_root(request)
            raw_articles = api.parse(root)

            try:
                for art in raw_articles:
                    article = api.to_dataframe(art)
                    dfs.append(article)

            except:
                switch = False

            start += 10
df = pd.concat(dfs, ignore_index=True)
df.to_csv('../software_data.csv')

