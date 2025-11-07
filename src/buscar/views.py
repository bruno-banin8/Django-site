import requests
from django.shortcuts import render, redirect
from urllib.parse import quote # CORREÇÃO: Importar 'quote' da biblioteca padrão Python
from .models import User

def get_youtube_search_url(banda, musica):
    query = f"{banda} - {musica} official video"
    return f"https://www.youtube.com/results?search_query={quote(query)}"
    
def index(request):
    return render(request, 'index.html')


def resultado(request):
    if request.method == 'POST':
        banda = request.POST.get('banda')
        tipo_busca = request.POST.get('tipo')
        termo = request.POST.get('termo') or ''

        banda_lower = banda.strip().lower()
        termo_lower = termo.strip().lower()

        url = f"https://itunes.apple.com/search?term={quote(banda)}&entity=song&attribute=artistTerm"

        resposta = requests.get(url)
        dados = resposta.json()
        resultados_nao_filtrados = dados.get('results', [])

        resultados_filtrados = []
        resultados_com_link = []
        banda_original = banda # Usa o nome da banda da busca inicial
        albuns_vistos = set() # Variável para filtrar álbuns duplicados
        banda_encontrada = False
        
        if tipo_busca == 'musica':    
            for item in resultados_nao_filtrados:
                if 'artistName' in item and item['artistName'].strip().lower() == banda_lower: # Apenas para resultados que são músicas
                    banda_encontrada = True
                    if item['trackName'].strip().lower() == termo_lower:
                        resultados_filtrados.append(item)
        elif tipo_busca == 'album':
            for item in resultados_nao_filtrados:
                if 'artistName' in item and item['artistName'].strip().lower() == banda_lower: # Apenas para resultados que são músicas
                    banda_encontrada = True
                    collection_id = item.get('collectionId')

                    if collection_id and collection_id not in albuns_vistos:
                        albuns_vistos.add(collection_id)
                        resultados_filtrados.append(item)
        else:
            for item in resultados_nao_filtrados:
                if 'artistName' in item and item['artistName'].strip().lower() == banda_lower:
                    banda_encontrada = True
                    resultados_filtrados.append(item)
        

        for item in resultados_filtrados:
            if 'trackName' in item: # Apenas para resultados que são músicas
                item['youtube_link'] = get_youtube_search_url(banda_original, item['trackName'])
            resultados_com_link.append(item)
            
        resultados = resultados_com_link

        return render(request, 'resultado.html', {
            'banda': banda,
            'tipo_busca': tipo_busca,
            'resultados': resultados,
            'banda_encontrada': banda_encontrada
        })



def musicas_album(request, album_id):
    # Lógica que busca a banda original (se você implementou a correção anterior)
    banda_original = request.GET.get('banda')
    
    url = f"https://itunes.apple.com/lookup?id={album_id}&entity=song"
    resposta = requests.get(url)
    dados = resposta.json()
    resultados = dados.get('results', [])

    if resultados:
        album_info = resultados[0]
        album_musicas = resultados[1:]

        # Se a banda não foi passada via GET, tenta pegar do primeiro item da lista
        if not banda_original:
            banda_original = album_musicas[0].get('artistName', '')

        # 2. ADICIONAR O LINK DO YOUTUBE A CADA MÚSICA
        musicas_com_link = []
        for musica in album_musicas:
            if 'trackName' in musica:
                musica['youtube_link'] = get_youtube_search_url(banda_original, musica['trackName'])
            musicas_com_link.append(musica)
            

    else:
        album_info = None
        musicas_com_link = []

    return render(request, 'musicas_album.html', {
        'album': album_info,
        'musicas': musicas_com_link
    })

def login(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        e = request.POST.get('email')

        u = User(name=nome, email=e)
        u.save()


        return redirect('index')
    return render(request, 'login.html')