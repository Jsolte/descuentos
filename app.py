import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="rebajas 3º ESO", page_icon="🖩")

# Título y Descripción
st.title("🖩 Calculadora de rebajas")
st.markdown("Bienvenido. Introduce tus datos para calcular el precio final despues de la rebaja.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio_original = st.sidebar.number_input("el precio €", min_value=0, max_value=1000, value=60)
descuento = st.sidebar.slider("la rebaja %)", 1.00, 100.00)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    ahorro = precio_original * (descuento / 100)
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu ahorro es:", value=f"{ahorro:.2f}")
        
 
            
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' descuento = \frac{precio_original}{descuento/100} ''')
