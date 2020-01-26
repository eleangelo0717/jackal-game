"use strict"

let serverdata = {}
let selectedItem = ''
let selectedPayload = ''
let api_url = '/api/'

function getData() {
    fetch(api_url, {
        cache: 'no-cache',
    })
        .then(response => {
            const contentType = response.headers.get('content-type')
            if (!contentType || !contentType.includes('application/json')) {
                throw new TypeError("Oops, we haven't got JSON!")
            }
            return response.json()
        })
        .then(data => {
            serverdata = data
            refresh()
        })
}

function sendMoveData(itemId, coord, payloadIds) {
    let data = [{
        'item': itemId,
        'x': coord[1],
        'y': coord[0]
    }]
    if (payloadIds) {
        for (let p in payloadIds) {
            if (payloadIds[p] !== '') {
                data.push({
                    'item': payloadIds[p],
                    'x': coord[1],
                    'y': coord[0]
                })
            }
        }
    }
    fetch(api_url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
        cache: 'no-cache',
    })
        .then(response => {
            const contentType = response.headers.get('content-type')
            if (!contentType || !contentType.includes('application/json')) {
                throw new TypeError("Oops, we haven't got JSON!")
            }
            return response.json()
        })
        .then(data => {
            serverdata = data
            refresh()
        })
}

function refresh() {
    let field = document.getElementById("field")
    if (!(field.getElementsByClassName('place').length)) {
        fillField(field)
    }
    refreshField(field)
    fillItems(field)
}

function fillField(field) {
    for (let y in serverdata.field) {
        let row = document.createElement("div")
        row.setAttribute("class", "row")
        field.appendChild(row)
        for (let x in serverdata.field[y]) {
            row.appendChild(newTile(y, x, serverdata.field[y][x]))
        }
    }
}

function fillItems(field) {
    for (let key in serverdata.items) {
        let item = serverdata.items[key]
        let placeID = generatePlaceID(item.y, item.x)
        let div = document.getElementById(generateItemID(key))
        if (!(div)) {
            div = document.createElement("div")

            div.setAttribute("class", `item ${item.type} gamer_${item.gamer} hidden`)
            div.setAttribute("id", generateItemID(key))
            if (item.type) {
                let img = document.createElement("img")
                switch (item.type) {
                    case "Pirate":
                        img.setAttribute("src", `images/pirate${item.gamer}.png`)
                        break
                    case "Ship":
                        img.setAttribute("src", `images/ship${item.gamer}.png`)
                        div.classList.add('payload')
                        break
                    case "Coin":
                        img.setAttribute("src", `images/coin.png`)
                        div.classList.add('payload')
                        break
                    case "Chest":
                        img.setAttribute("src", `images/chest.png`)
                        div.classList.add('payload')
                        break
                }
                img.addEventListener('click', function (event) { selectItem(event) }, false)
                div.appendChild(img)
            }
            field.appendChild(div)
        }
        if (placeID) {
            let place = document.getElementById(placeID)
            placeItem(div, place)
        }
    }
    repaintItems()
}


function selectPlace(e) {
    if (selectedItem) {
        placeItem(selectedItem, e.target.parentNode, true)
    }
}

function placeItem(item, place, send_data) {
    if (item.parentNode === place) {
        return
    }

    let payloads = []
    if (selectedPayload) {
        payloads.push(selectedPayload)
        if (selectedPayload.classList.contains('Ship')) {
            for (let payloadClass of ['Pirate', 'Coin', 'Chest']) {
                for (let p of Array.from(selectedItem.parentNode.getElementsByClassName(payloadClass))) {
                    if (p !== item) {
                        payloads.push(p)
                    }
                }
            }
        }
    }

    setTimeout(function () {
        let placeRect = place.getBoundingClientRect()
        moveItemStage1(item, placeRect)
        let itemRect = item.getBoundingClientRect()
        for (let p of payloads) {
            moveItemStage1(p, placeRect)
        }
    }, 100)

    setTimeout(function () {
        moveItemStage2(item, place)
        for (let p of payloads) {
            moveItemStage2(p, place)
        }
        if (send_data) {
            sendMoveData(item.id.split('_')[1], place.id.split(':'), payloads.map(x => x.id.split('_')[1]))
        }
        clearSelection()
    }, 500)
}

function moveItemStage1(item, placeRect) {
    let itemRect = item.getBoundingClientRect()
    item.classList.remove('hidden')
    item.style.bottom = `${itemRect.top - placeRect.top}px`
    item.style.left = `${placeRect.left - itemRect.left}px`
}

function moveItemStage2(item, place) {
    item.style.bottom = 0
    item.style.left = 0
    place.appendChild(item)
}

function selectItem(e) {
    console.log(e)
    let targetItem = e.target.parentNode
    if (selectedItem) {
        if (selectedItem.parentNode === targetItem.parentNode) {
            if (e.altKey) {
                selectNextPayloadInPlace()
            } else {
                selectNextItemInPlace()
            }
        } else {
            placeItem(selectedItem, targetItem.parentNode, true)
        }
    } else {
        if (targetItem.classList.contains('Pirate')) {
            setItemSelected(targetItem)
        }
    }
}

function setItemSelected(item) {
    clearSelection()
    selectedItem = item
    selectedItem.classList.add('selected')
    let s = document.getElementById('selection')
    let pirateDiv = document.createElement("div")
    let img = document.createElement("img")
    img.setAttribute("src", selectedItem.firstChild.getAttribute("src"))
    pirateDiv.appendChild(img)
    s.appendChild(pirateDiv)
}

function setPayloadSelected(item) {
    clearPayloadSelection()
    selectedPayload = item
    selectedPayload.classList.add('selected')
    let s = document.getElementById('selection')
    let payloadDiv = document.createElement("div")
    let img = document.createElement("img")
    img.setAttribute("src", selectedPayload.firstChild.getAttribute("src"))
    payloadDiv.classList.add("payload")
    payloadDiv.appendChild(img)
    s.appendChild(payloadDiv)
}


function getItemGamer(item) {
    c = [...item.classList].filter(x => x.match(/gamer_*/))
    return c.length && c[0]
}

function selectNextItemInPlace() {
    let pirates = Array.from(selectedItem.parentNode.getElementsByClassName('Pirate'))
    for (let i in pirates) {
        if (pirates[i] === selectedItem) {
            selectedItem.classList.remove('selected')
            if (i > 0) {
                setItemSelected(pirates[i - 1])
            } else {
                clearSelection()
            }
        }
    }
}

function selectNextPayloadInPlace() {
    if (!(selectedItem)) {
        return
    }
    let payloads = Array.from(selectedItem.parentNode.getElementsByClassName('payload'))
    if (!(selectedPayload) && payloads.length) {
        setPayloadSelected(payloads[payloads.length - 1])
        return
    }
    for (let i in payloads) {
        if (payloads[i] === selectedPayload) {
            selectedPayload.classList.remove('selected')
            if (i > 0) {
                setPayloadSelected(payloads[i - 1])
            } else {
                clearPayloadSelection()
            }
        }
    }
}

function clearSelection() {
    selectedItem = ''
    let items = Array.from(document.getElementById("field").getElementsByClassName('Pirate'))
    items.map(x => {
        x.classList.remove('selected')
    })
    let s = document.getElementById('selection')
    while (s.firstChild) {
        s.removeChild(s.firstChild);
    }
    repaintItems()
    clearPayloadSelection()
}

function clearPayloadSelection() {
    selectedPayload = ''
    let items = Array.from(document.getElementById("field").getElementsByClassName('payload'))
    items.map(x => {
        x.classList.remove('selected')
    })
}

function repaintItems() {
    let items = Array.from(document.getElementById("field").getElementsByClassName('item'))
    items.map(x => {
        let pirates = Array.from(x.parentNode.getElementsByClassName('Pirate'))
        if (pirates.length > 1) {
            x.classList.add('multi')
            pirates.map((x, i) => {
                x.style.left = `${i * 40 / pirates.length}%`
                x.style.bottom = `${i * 15 / pirates.length}%`
            })
        } else {
            x.classList.remove('multi')
            x.style.left = 0
            x.style.bottom = 0
        }
    })
}

function generateItemID(key) {
    if (typeof (key) !== 'undefined') {
        return `item_${key}`
    }
    return
}

function generatePlaceID(row, col) {
    if (typeof (row) !== 'undefined' && typeof (col) !== 'undefined') {
        return `${row}:${col}`
    }
    return
}

function refreshField(field) {
    for (let y in serverdata.field) {
        for (let x in serverdata.field[y]) {
            let placeData = serverdata.field[y][x]
            let place = document.getElementById(generatePlaceID(y, x))
            let img = getImageName(placeData)
            if (img) {
                place.childNodes[0].setAttribute("src", img)
                if (placeData.orientation) {
                    place.classList.add(`rotate${placeData.orientation}`)
                }
            }
        }
    }
}

function getImageName(data) {
    if (data.type !== 'EXCLUDED') {
        let img = document.createElement("img")
        switch (data.type) {
            case "SEA":
                return "images/sea.png"
                break
            case "GROUND":
                if (data.tile && data.tile.type) {
                    return `images/classic-${toKebabCase(data.tile.type)}.png`
                } else {
                    return "images/classic-cover.webp"
                }
                break
            default:
                return "images/classic-boat.png"
        }
    }

}

function newTile(row, col, data) {
    let div = document.createElement("div")
    div.setAttribute("class", "place")
    div.setAttribute("id", generatePlaceID(row, col))
    if (data.type !== 'EXCLUDED') {
        if (data.type === 'GROUND') {
            div.classList.add('tile')
        }
        let img = document.createElement("img")
        img.setAttribute("src", getImageName(data))
        img.addEventListener('click', function (event) { selectPlace(event) },
            false)
        div.appendChild(img)
    }
    return div
}

function init() {
    getData()
    setInterval(function () { getData() }, 5000);
}

function toKebabCase(s) {
    return s && s.match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
        .map(x => x.toLowerCase())
        .join('-')
}

init()


