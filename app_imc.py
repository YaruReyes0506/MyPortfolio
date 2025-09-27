def calcular_imc(peso, altura):
    imc = peso / (altura ** 2) 
    return imc

def recomendacion(imc):
    if imc <18.5:
        estado = ["Peso Bajo"]
        alimentacion = ["•	Aumentar la ingesta calórica de forma saludable","•	Comer 5-6 veces al día (desayuno, media mañana, almuerzo, merienda, cena, snack nocturno).","•	Incluir alimentos ricos en proteínas: huevos, pescado, carnes magras, legumbres", "•	Añadir grasas saludables: aguacate, frutos secos, aceite de oliva.","•	Batidos de frutas con avena o leche entera como snack."]
        ejercicio = ["•	Ejercicios de fuerza/resistencia: pesas, ejercicios con peso corporal (flexiones, sentadillas).","•	Evitar cardio intenso; priorizar entrenamientos de fuerza 3-4 veces por semana.","•	Objetivo: aumentar masa muscular."]
        rutina = ["•	Despertarse temprano y hacer un desayuno nutritivo.","•	Comer cada 3 horas.","•	Realizar una rutina de fuerza por la tarde (45 minutos).","•	Dormir al menos 8 horas."]
        return estado,alimentacion,ejercicio,rutina
    

    if imc >=18.5 and imc <24.9:
        estado = ["Peso Normal"]
        alimentacion = ["•	Dieta balanceada: frutas, verduras, proteínas magras, carbohidratos integrales.","•	Controlar porciones y evitar excesos de azúcares y grasas.","•	Mantener buena hidratación (agua > 2L/día)."]
        ejercicio = ["•	Mezcla de ejercicio aeróbico (cardio) y fuerza.","o	Cardio: 150 min/semana (caminar, correr, bicicleta).","o	Fuerza: 2-3 veces por semana."]
        rutina = ["o Fuerza: 2-3 veces por semana.","•	3 comidas principales + 2 snacks saludables.","•	Dormir entre 7-9 horas."]
        return estado,alimentacion,ejercicio,rutina
    

    if imc >=25.00 and imc <29.9:
        estado = ["Sobrepeso"]  
        alimentacion = ["•	Reducir calorías: evitar fritos, refrescos, dulces.","•	Comer más vegetales, proteínas magras (pollo, pescado) y cereales integrales.","•	Evitar comidas procesadas y reducir sal."]
        ejercicio = ["•	Cardio moderado: caminar rápido, trotar suave, bici al menos 30-45 min diarios.","•	Introducir ejercicios de fuerza 2 veces por semana.","•	Aumentar movimiento durante el día (subir escaleras, caminar más)."]
        rutina = ["•	Desayuno saludable alto en fibra.","•   Ejercicio 5-6 veces por semana.","•	Evitar cenar tarde y controlar porciones.","•	Hidratación constante."]
        return estado,alimentacion,ejercicio,rutina


    if imc >=30.0 and imc <34.9:
        estado = ["Obsidad Grado 1"]
        alimentacion = ["•	Evitar comidas procesadas y reducir sal.","•	Comer lentamente y ser consciente de las porciones.","•	Eliminar bebidas azucaradas y comida rápida."]
        ejercicio = ["•	Iniciar con caminar 30 minutos al día, aumentar gradualmente.","•	Ejercicios de bajo impacto (natación, bicicleta estática).","•	Incorporar fuerza ligera 1-2 veces/semana."]
        rutina = ["•	Actividad física diaria adaptada.","•	Dormir bien (falta de sueño puede aumentar el apetito","•	Planificar comidas con anticipación.","•	Evaluación médica y control de presión, glucosa, etc."]
        return estado,alimentacion,ejercicio,rutina
    
    if imc >=35.0 and imc <39.9:
        estado = ["Obesidad Grado 2"]
        alimentacion = ["•	Dieta hipocalórica estricta guiada por especialista.","•	Reeducación alimentaria: identificar hábitos negativos.","•	Evitar snacks, alcohol, pan blanco, postres.","•	Introducir más vegetales, proteínas vegetales y frutas con bajo índice glucémico"]
        ejercicio = ["•	Comenzar con actividades suaves: caminatas diarias, yoga, ejercicios en silla si es necesario.","•	Apoyo profesional (fisioterapeuta, entrenador personal).","•	Avanzar gradualmente hacia sesiones más largas."]
        rutina = [ "•   Registrar comidas y actividad física.","•	Control médico frecuente.","•	Apoyo psicológico si hay relación emocional con la comida.","•	Establecer objetivos a corto plazo."]
        return estado, alimentacion, ejercicio, rutina
    
    if imc >=40.0:
        estado  = ["Obesidad Grado 3"]
        alimentacion = ["•	Supervisión médica y nutricional rigurosa.","•	Considerar tratamientos médicos (en algunos casos cirugía bariátrica).","•	Dieta muy controlada, evitar absolutamente todo tipo de comida procesada o calórica.","•	Plan de nutrición personalizada."]
        ejercicio = ["•	Actividad física adaptada a las limitaciones físicas actuales.","•	Comenzar con ejercicios en piscina o sentado, caminatas cortas.","•	Trabajo progresivo con profesionales."]
        rutina = ["•	Evaluaciones médicas frecuentes.","•	Terapia psicológica si es necesario.","•	Apoyo social o grupos de apoyo.","•	Establecer micro objetivos diarios (p. ej., caminar 5 minutos más cada semana)."]
        return estado,alimentacion,ejercicio,rutina
    
