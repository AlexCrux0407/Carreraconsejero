// JavaScript para CareerAdvisor

document.addEventListener('DOMContentLoaded', function() {
    // Animación para el botón de análisis
    const analyzeButton = document.querySelector('.btn-primary');
    if (analyzeButton) {
        analyzeButton.addEventListener('mouseover', function() {
            this.classList.add('pulse');
        });
        
        analyzeButton.addEventListener('mouseout', function() {
            this.classList.remove('pulse');
        });
        
        analyzeButton.addEventListener('click', function() {
            // Mostrar un mensaje de carga mientras se analiza el hardware
            if (this.getAttribute('href') === '/analyze') {
                this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Analizando...';
                this.classList.add('disabled');
            }
        });
    }
    
    // Añadir tooltips para mostrar información adicional
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    if (typeof bootstrap !== 'undefined') {
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
    
    // Funcionalidad para compartir resultados (simulada)
    const shareButtons = document.querySelectorAll('.share-btn');
    shareButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            alert('¡Compartir resultados no está disponible en esta versión de demostración!');
        });
    });
    
    // Activar tooltips de Bootstrap si están disponibles
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});

// Función para copiar los resultados al portapapeles (simulada)
function copyResults() {
    alert('Resultados copiados al portapapeles (simulado)');
    // Aquí iría la implementación real con la API Clipboard
}