const BIST100_SYMBOLS = ["GARAN", "AKBNK", "THYAO", "SISE", "KRDMD", "ISCTR", "ASELS", "BIMAS", "FROTO", "TUPRS"];
let selectedSymbol = "GARAN";

function fetchFavorites() {
    fetch('/api/favorites')
        .then(r => r.json())
        .then(data => {
            const list = document.getElementById('favorites-list');
            list.innerHTML = '';
            data.forEach(fav => {
                const li = document.createElement('li');
                li.className = 'list-group-item d-flex justify-content-between align-items-center';
                li.innerHTML = `${fav.symbol} <span>${fav.data ? fav.data.price : ''}</span>`;
                li.onclick = () => { selectedSymbol = fav.symbol; updateCharts(); };
                const delBtn = document.createElement('button');
                delBtn.className = 'btn btn-sm btn-danger';
                delBtn.innerText = 'Sil';
                delBtn.onclick = (e) => { e.stopPropagation(); deleteFavorite(fav.symbol); };
                li.appendChild(delBtn);
                list.appendChild(li);
            });
        });
}

function addFavorite() {
    fetch('/api/favorites', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ symbol: selectedSymbol })
    }).then(fetchFavorites);
}

function deleteFavorite(symbol) {
    fetch(`/api/favorites/${symbol}`, { method: 'DELETE' }).then(fetchFavorites);
}

document.getElementById('add-fav-btn').onclick = addFavorite;

document.getElementById('symbol-search').addEventListener('input', function() {
    const val = this.value.toUpperCase();
    const match = BIST100_SYMBOLS.find(s => s.startsWith(val));
    if (match) selectedSymbol = match;
});

let mainChart, rsiChart, macdChart;

function updateCharts() {
    fetch(`/api/quote/${selectedSymbol}`)
        .then(r => r.json())
        .then(data => {
            // Sadece fiyat için örnek, TA entegre edildiğinde güncellenecek
            if (!mainChart) {
                mainChart = new Chart(document.getElementById('mainChart').getContext('2d'), {
                    type: 'line',
                    data: { labels: [selectedSymbol], datasets: [{ label: 'Fiyat', data: [data.price], borderColor: 'blue' }] },
                });
            } else {
                mainChart.data.labels = [selectedSymbol];
                mainChart.data.datasets[0].data = [data.price];
                mainChart.update();
            }
        });
}

fetchFavorites();
updateCharts();
setInterval(() => { fetchFavorites(); updateCharts(); }, 15000); 