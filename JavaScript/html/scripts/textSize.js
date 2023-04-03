function makeSizer(size) {
    return function () {
        document.body.style.fontSize = `${size}px`;
    };
}

const size12 = makeSizer(12);
const size14 = makeSizer(14);
const size16 = makeSizer(16);

document.getElementById("size12").onClick = size12;
document.getElementById("size-14").onClick = size14;