// diccionarios
const subcategorias = {
    plastico: ["Botellas", "Envases", "Bolsas"],
    papel: ["Periodicos", "Carton", "Papel de oficina"],
    vidrio: ["Botellas", "Frascos", "Cristaleria"],
    metales: ["Latas", "Cables", "Electrodomesticos pequeños"],
    electronicos: ["Telefonos moviles", "Baterias", "Componentes de computadoras"]
};

// actualizar subcategorias 
document.getElementById('tipoResiduo').addEventListener('change', function() {
    const tipoSeleccionado = this.value;
    const subcategoriaSelect = document.getElementById('subcategoriaResiduo');
    
    // limpiar las opciones actuales
    subcategoriaSelect.innerHTML = '<option value="">Seleccione una subcategoría</option>';

    if (subcategorias[tipoSeleccionado]) {
        // añadir las nuevas subcategorias
        subcategorias[tipoSeleccionado].forEach(function(subcategoria) {
            const option = document.createElement('option');
            option.value = subcategoria.toLowerCase();
            option.textContent = subcategoria;
            subcategoriaSelect.appendChild(option);
        });
    }
});

// validacion del formulario
document.getElementById('formulario_reciclaje').addEventListener('submit', function(event) {
    // Prevenir envio del formulario si hay errores
    let valid = true;

    if (valid) {
        alert("Formulario enviado correctamente");
    }
});
