document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const manufacturer = document.getElementById('manufacturer').value;
            const type_number = document.getElementById('type_number').value;
            const project = document.getElementById('project').value;
            const order_processor = document.getElementById('order_processor').value;
            const date_of_purchase = document.getElementById('date_of_purchase').value;
            const storage_period = document.getElementById('storage_period').value;
            const value_before_tax = document.getElementById('value_before_tax').value;
            const tax_rate = document.getElementById('tax_rate').value;
            const location = document.getElementById('location').value;

            if (!name || !manufacturer || !type_number || !project || !order_processor || !date_of_purchase || !storage_period || !value_before_tax || !tax_rate || !location) {
                alert('Please fill out all fields.');
                event.preventDefault();
            }
        });
    }

    // Delete confirmation
    const deleteLinks = document.querySelectorAll('a[href^="/delete/"]');
    deleteLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this product?')) {
                event.preventDefault();
            }
        });
    });

    // Dynamic field calculation (if needed)
    const valueBeforeTaxInput = document.getElementById('value_before_tax');
    const taxRateInput = document.getElementById('tax_rate');
    const taxableValueDisplay = document.getElementById('taxable_value');

    if (valueBeforeTaxInput && taxRateInput && taxableValueDisplay) {
        function calculateTaxableValue() {
            const valueBeforeTax = parseFloat(valueBeforeTaxInput.value) || 0;
            const taxRate = parseFloat(taxRateInput.value) || 0;
            const taxableValue = valueBeforeTax * (1 + taxRate / 100);
            taxableValueDisplay.textContent = taxableValue.toFixed(2);
        }

        valueBeforeTaxInput.addEventListener('input', calculateTaxableValue);
        taxRateInput.addEventListener('input', calculateTaxableValue);
    }
});
