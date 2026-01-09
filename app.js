const API = "https://fpvchimes-python-api.onrender.com";

let melody = [];
let audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function add(note) {
    melody.push(`${note} 8`);
    document.getElementById("melody").innerText = melody.join(" ");
    playNote(note, 0.3);
}

function noteToFreq(note) {
    const notes = {
        'C5': 523.25, 'D5': 587.33, 'E5': 659.25, 'F5': 698.46,
        'G5': 783.99, 'A5': 880.00
    };
    return notes[note] || 440;
}

function playNote(note, duration) {
    let oscillator = audioCtx.createOscillator();
    oscillator.type = 'square';
    oscillator.frequency.setValueAtTime(noteToFreq(note), audioCtx.currentTime);
    oscillator.connect(audioCtx.destination);
    oscillator.start();
    oscillator.stop(audioCtx.currentTime + duration);
}

async function upload() {
    await fetch(`${API}/songs`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: name.value,
            author: author.value,
            melody: melody.join(" ")
        })
    });
    melody = [];
    load();
}

async function load() {
    const res = await fetch(`${API}/songs`);
    const songs = await res.json();
    const songsList = document.getElementById("songs");
    songsList.innerHTML = songs.map(
        s => `<li>
                <b>${s.name}</b> (${s.likes} likes) — ${s.melody}
                <button onclick="like('${s.name}')">❤️ Like</button>
                <button onclick="exportSong('${s.name}','${s.melody}')">⬇️ Export</button>
               </li>`
    ).join("");
}

async function like(name) {
    await fetch(`${API}/songs/${name}/like`, { method: "POST" });
    load();
}

function exportSong(name, melody) {
    const blob = new Blob([melody], {type: "text/plain"});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `${name}.txt`;
    a.click();
}

load();

