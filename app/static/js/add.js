const totalElements = document.querySelectorAll('.product-line-price');
const increaseBtns = document.querySelectorAll('.increaseQty');
const decreaseBtns = document.querySelectorAll('.decreaseQty');
const quantityInputs = document.querySelectorAll('.product-quantity');

let grandTotal = 0;
let promo = 2284.20; // Définissez la valeur du rabais
let chargeLivraison = 25.00; // Définissez le coût de livraison
let tauxTaxe = 0.125; // Définissez le taux de taxe

increaseBtns.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        const currentQuantity = parseInt(quantityInputs[index].value);
        quantityInputs[index].value = currentQuantity + 1;
        updateTotal(index, currentQuantity + 1);
    });
});

decreaseBtns.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        const currentQuantity = parseInt(quantityInputs[index].value);
        if (currentQuantity > 0) {
            quantityInputs[index].value = currentQuantity - 1;
            updateTotal(index, currentQuantity - 1);
        }
    });
});

function updateTotal(index, quantity) {
    let price = parseFloat(document.querySelectorAll('.product-price')[index].textContent);
    if (quantity === 0) {
        price = 0; // Si la quantité est égale à zéro, mettre le prix à zéro
    }
    const total = quantity * price;
    totalElements[index].textContent = total.toFixed(2);
    calculateGrandTotal();
}

function calculateGrandTotal() {
    let subtotal = 0;
    totalElements.forEach(element => {
        subtotal += parseFloat(element.textContent);
    });

    const tax = subtotal * tauxTaxe;
    const totalBeforeDiscount = subtotal + tax + chargeLivraison;
    const totalAfterDiscount = totalBeforeDiscount - promo;

    document.getElementById('cart-subtotal').textContent = `${subtotal.toFixed(2)} CFA`;
    document.getElementById('cart-discount').textContent = `-${promo.toFixed(2)} FCFA`;
    document.getElementById('cart-shipping').textContent = `${chargeLivraison.toFixed(2)} FCFA`;
    document.getElementById('cart-tax').textContent = `${tax.toFixed(2)} FCFA`;
    document.getElementById('cart-total').textContent = `${totalAfterDiscount.toFixed(2)} FCFA`;
}
