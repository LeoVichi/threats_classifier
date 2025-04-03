import feedparser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from colorama import Fore, Style

# 1. Definir URL de RSS Feed (BBC como exemplo)
rss_url = "https://feeds.bbci.co.uk/news/world/rss.xml"

# 2. Coletar notícias
feed = feedparser.parse(rss_url)
texts = [entry['title'] + ' ' + entry.get('summary', '') for entry in feed.entries[:10]]

print(f"\n📰 Coletadas {len(texts)} manchetes do RSS\n")

# 3. Base de treinamento simples
train_texts = [
    "Cyberattack on government systems.",
    "Massive data leak threatens national security.",
    "Peace treaty signed by two nations.",
    "Tourism booming after pandemic recovery.",
    "Threats to power grid detected.",
    "Holiday celebrations bring people together.",
]
train_labels = [1, 1, 0, 0, 1, 0]  # 1 = ameaça, 0 = inofensivo

# 4. Treinamento do modelo
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])
model.fit(train_texts, train_labels)

# 5. Classificação dos textos coletados
predictions = model.predict(texts)

# 6. Exibição dos resultados
for i, (text, pred) in enumerate(zip(texts, predictions), 1):
    label = f"{Fore.RED}⚠️ Ameaça" if pred else f"{Fore.GREEN}✅ Inofensivo"
    print(f"{Style.BRIGHT}{i:02d}. {text[:100].strip()}...\n{label}{Style.RESET_ALL}\n")

