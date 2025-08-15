function osszegSzamitas() {
    const elso = parseFloat(document.getElementById('elsoSzam').value) || 0;
    const masodik = parseFloat(document.getElementById('masodikSzam').value) || 0;
    const osszeg = elso + masodik;
    document.getElementById('eredmeny').textContent = `Eredmény: ${osszeg}`;
}

function kulonbsegSzamitas() {
    const elso = parseFloat(document.getElementById('elsoSzam').value) || 0;
    const masodik = parseFloat(document.getElementById('masodikSzam').value) || 0;
    const kulonbseg = elso - masodik;
    document.getElementById('eredmeny').textContent = `Eredmény: ${kulonbseg}`;
}

function szorzatSzamitas() {
    const elso = parseFloat(document.getElementById('elsoSzam').value) || 0;
    const masodik = parseFloat(document.getElementById('masodikSzam').value) || 0;
    const szorzat = elso * masodik;
    document.getElementById('eredmeny').textContent = `Eredmény: ${szorzat}`;
}

function hanyadosSzamitas() {
    const elso = parseFloat(document.getElementById('elsoSzam').value) || 0;
    const masodik = parseFloat(document.getElementById('masodikSzam').value) || 0;
    let hanyados;
    if (masodik === 0) {
        hanyados = 'Nullával nem lehet osztani!';
    } else {
        hanyados = elso / masodik;
    }
    document.getElementById('eredmeny').textContent = `Eredmény: ${hanyados}`;
}
