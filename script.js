const menu = [
    { id: 1, name: 'Pizza', price: 12.99 },
    { id: 2, name: 'Burger', price: 8.99 },
    { id: 3, name: 'Pasta', price: 10.99 },
    { id: 4, name: 'Salad', price: 7.99 },
    { id: 5, name: 'Soda', price: 1.99 }
  ];
  
  let order = [];
  
  function renderMenu() {
    const menuDiv = document.getElementById('menu-items');
    menu.forEach(item => {
      const card = document.createElement('div');
      card.className = 'menu-card';
      card.innerHTML = `
        <h3>${item.name}</h3>
        <p>Price: $${item.price.toFixed(2)}</p>
        <button onclick="addToOrder(${item.id})">Add to Cart</button>
      `;
      menuDiv.appendChild(card);
    });
  }
  
  function addToOrder(id) {
    const item = menu.find(i => i.id === id);
    const existing = order.find(i => i.id === id);
    if (existing) {
      existing.quantity += 1;
      existing.total = existing.quantity * item.price;
    } else {
      order.push({ ...item, quantity: 1, total: item.price });
    }
    updateOrderList();
  }
  
  function updateOrderList() {
    const list = document.getElementById('order-list');
    list.innerHTML = '';
    let total = 0;
    order.forEach(item => {
      const li = document.createElement('li');
      li.textContent = `${item.name} x${item.quantity} = $${item.total.toFixed(2)}`;
      list.appendChild(li);
      total += item.total;
    });
    document.getElementById('total-price').textContent = `Total: $${total.toFixed(2)}`;
  }
  
  function applyDiscount() {
    const code = document.getElementById('discount-code').value.trim();
    let total = order.reduce((sum, item) => sum + item.total, 0);
    if (code === 'SAVE10') {
      total *= 0.9;
      alert('10% discount applied!');
    } else if (code) {
      alert('Invalid discount code');
    }
    document.getElementById('total-price').textContent = `Total: $${total.toFixed(2)}`;
  }
  
  function confirmOrder() {
    if (order.length === 0) {
      alert('Your order is empty!');
      return;
    }
    alert('Thank you for your order!');
    order = [];
    updateOrderList();
    document.getElementById('discount-code').value = '';
  }
  
  window.onload = renderMenu;
  