# Acciones para completar el perfil

## Integrar las propuestas

Cada repositorio tiene una propuesta en la rama `docs/mejoras-perfil`.
Revisar el diff y los checks de cada PR antes de integrarlo.
El README del perfil y los badges de la rama principal se actualizan al integrar los PR correspondientes.
No se ha modificado la bio, fijado repositorios ni cambiado su visibilidad.

## Configuración manual de GitHub

- Fijar los seis proyectos de la tabla del perfil: DolarToApp, Gastos-Compartidos, Gastos-Compartidos-Flutter, StitchHub, Puente_Flutter y scriptor-digital.
- Actualizar la bio a: **iOS Developer (Swift, SwiftUI) | Full Stack: Next.js, Supabase | Argentina**.
- Mantener el mismo foco en el CV y otros perfiles profesionales.
- Agregar enlaces oficiales de apps publicadas cuando existan; una política de privacidad o un repo no equivale a una ficha en una tienda.
- Decidir personalmente si algún repositorio de aprendizaje, duplicado o antiguo debe archivarse. Esta propuesta no archiva, elimina ni cambia la privacidad de ningún repo.
- Revisar las descripciones de About: faltan en los dos proyectos Flutter destacados.
- Confirmar la cuenta y los datos del entorno de desarrollo usados por los E2E existentes de StitchHub. Sus credenciales van en secretos de Actions, nunca en el README.

## Fechas y experiencia

Luciano confirmó que DolarToApp está publicada en App Store. Se incorpora como proyecto destacado; falta añadir el enlace oficial a la ficha. No se agregan fechas, descargas ni valoraciones.

Se retiró «Trabajo con Swift desde 2018»: hay un commit público y código Swift de 2017 en PruebaRepositorio,
pero eso no confirma el inicio exacto en 2018 ni continuidad de empleo profesional.
Si se agrega una fecha, verificarla con antecedentes propios.
No se añadieron empleadores, clientes, métricas ni años de experiencia.

## Marcadores por completar

Los marcadores de configuración se reemplazan en el entorno local, no con credenciales reales dentro de la documentación pública.
Cuando no exista una publicación, reemplazar el marcador correspondiente por «En desarrollo; sin publicación pública».

| Repo / archivo | Marcador o información pendiente |
| --- | --- |
| Perfil / README | [COMPLETAR: experiencia previa o trabajos con clientes] |
| Perfil / README | [COMPLETAR: enlace a DolarToApp en App Store] |
| Perfil / README | [COMPLETAR: enlace de publicación iOS si existe] |
| Perfil / README | [COMPLETAR: enlace de publicación Android si existe] |
| Perfil / README | [COMPLETAR: demo instalable o publicación de Puente si existe] |
| Gastos-Compartidos / README | [COMPLETAR: captura de la lista de grupos, carga de gasto y balances en un simulador iOS] |
| Gastos-Compartidos / README | [COMPLETAR: enlace a App Store o TestFlight si existe una publicación] |
| Gastos-Compartidos-Flutter / README | [COMPLETAR: capturas de grupos, carga multidivisa y liquidaciones de la versión Flutter] |
| Gastos-Compartidos-Flutter / README | [COMPLETAR: enlace a Google Play o programa de pruebas si existe una publicación] |
| Puente_Flutter / README | [COMPLETAR: capturas reales de Inicio, Conversación y Confirmar información] |
| Puente_Flutter / README | [COMPLETAR: enlace a demo instalable o tienda si existe una publicación] |
| scriptor-digital / README | [COMPLETAR: captura de la portada y del formulario de contacto en escritorio y móvil] |
| SwiftUI_SignUp / README | [COMPLETAR: referencias del ejercicio y atribución o licencia de los recursos visuales] |
| StitchHub / README, ejemplo de .env.local | [COMPLETAR: URL del proyecto Supabase de desarrollo] |
| StitchHub / README, ejemplo de .env.local | [COMPLETAR: clave pública anon del entorno de desarrollo] |
| StitchHub / README | [COMPLETAR: procedimiento reproducible y verificado de preparación de Supabase, incluidos buckets, políticas y redirects] |

## Criterio de presentación

Priorizar capturas reales, instrucciones reproducibles y decisiones técnicas verificables.
No afirmar que una app está publicada, tiene usuarios, cumple métricas o ha sido validada en dispositivos sin evidencia.
La existencia de tests o un workflow no equivale a una ejecución exitosa: revisar los resultados del PR.
