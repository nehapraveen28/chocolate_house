// Elements
const flavorsList = document.getElementById("flavors-list");
const addFlavorBtn = document.getElementById("add-flavor-btn");
const addFlavorForm = document.getElementById("add-flavor-form");
const cancelFlavorBtn = document.getElementById("cancel-flavor-btn");
const flavorForm = document.getElementById("flavor-form");
const feedbackForm = document.getElementById("feedback-form");

// Fetch all seasonal flavors
const getFlavors = async () => {
    const response = await fetch('/flavors');
    const flavors = await response.json();

    if (flavors.message) {
        flavorsList.innerHTML = `<p>${flavors.message}</p>`;
    } else {
        flavorsList.innerHTML = flavors.map(flavor => {
            return `
                <div class="flavor-card">
                    <h3>${flavor.flavor_name}</h3>
                    <p>Start Date: ${flavor.start_date}</p>
                    <p>End Date: ${flavor.end_date}</p>
                    <p>Status: ${flavor.availability === 1 ? 'Available' : 'Not Available'}</p>
                    <button onclick="deleteFlavor(${flavor.id})">Delete</button>
                </div>
            `;
        }).join('');
    }
};

// Add flavor form submit handler
flavorForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const flavorName = document.getElementById('flavor-name').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const availability = document.getElementById('availability').value;

    const response = await fetch('/flavors', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            flavor_name: flavorName,
            start_date: startDate,
            end_date: endDate,
            availability: availability
        })
    });

    const result = await response.json();
    alert(result.message);
    if (response.ok) {
        getFlavors();
        flavorForm.reset();
        addFlavorForm.classList.add('hidden');
    }
});

// Show Add Flavor Form
addFlavorBtn.addEventListener('click', () => {
    addFlavorForm.classList.remove('hidden');
});

// Cancel Add Flavor Form
cancelFlavorBtn.addEventListener('click', () => {
    addFlavorForm.classList.add('hidden');
});

// Delete a flavor
const deleteFlavor = async (flavorId) => {
    const response = await fetch(`/flavors/${flavorId}`, {
        method: 'DELETE'
    });

    const result = await response.json();
    alert(result.message);
    if (response.ok) {
        getFlavors();
    }
};

// Add customer feedback
feedbackForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const customerName = document.getElementById('customer-name').value;
    const flavorSuggestion = document.getElementById('flavor-suggestion').value;
    const allergyConcern = document.getElementById('allergy-concern').value;

    const response = await fetch('/feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            customer_name: customerName,
            flavor_suggestion: flavorSuggestion,
            allergy_concern: allergyConcern
        })
    });

    const result = await response.json();
    alert(result.message);
    if (response.ok) {
        feedbackForm.reset();
    }
});

// Initial fetch to display all flavors
getFlavors();
