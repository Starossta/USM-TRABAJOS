// Diccionarios
const subcategorias = {
    plastico: ["Botellas", "Envases", "Bolsas"],
    papel: ["Periodicos", "Carton", "Papel de oficina"],
    vidrio: ["Botellas", "Frascos", "Cristaleria"],
    metales: ["Latas", "Cables", "Electrodomesticos pequeños"],
    electronicos: ["Telefonos moviles", "Baterias", "Componentes de computadoras"]
};

// Actualizar subcategorias 
document.getElementById('tipoResiduo').addEventListener('change', function() {
    const tipoSeleccionado = this.value;
    const subcategoriaSelect = document.getElementById('subcategoriaResiduo');
    
    // Limpiar las opciones actuales
    subcategoriaSelect.innerHTML = '<option value="">Seleccione una subcategoría</option>';

    if (subcategorias[tipoSeleccionado]) {
        // Añadir las nuevas subcategorias
        subcategorias[tipoSeleccionado].forEach(function(subcategoria) {
            const option = document.createElement('option');
            option.value = subcategoria.toLowerCase();
            option.textContent = subcategoria;
            subcategoriaSelect.appendChild(option);
        });
    }
});

// Validación del formulario
document.getElementById('formulario_reciclaje').addEventListener('submit', function(event) {
    // Prevenir envío del formulario si hay errores
    event.preventDefault();
    let valid = true;

    if (valid) {
        alert("Formulario enviado correctamente");
    }
});
