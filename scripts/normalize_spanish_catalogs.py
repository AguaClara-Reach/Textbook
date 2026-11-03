"""Normalize safe, recurring errors in Spanish PO translations.

The replacements here are deliberately limited to forms that are always wrong in
the AguaClara textbook.  The script decodes complete ``msgstr`` values first so
that it also finds phrases split across PO continuation lines.
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import warnings


RULES = (
    (re.compile(r"\bflóclos\b", re.I), "flóculos"),
    (re.compile(r"\bflóculum\b", re.I), "flóculo"),
    (re.compile(r"\bflocas\b", re.I), "flóculos"),
    (re.compile(r"\bflóc\b", re.I), "flóculo"),
    (re.compile(r"\bfloco\b", re.I), "flóculo"),
    (re.compile(r"\bflocos\b", re.I), "flóculos"),
    (
        re.compile(r"\benrollamiento de flóculos?\b", re.I),
        "arrastre ascendente de flóculos",
    ),
    (
        re.compile(r"\benrollamiento de floc\b", re.I),
        "arrastre ascendente de flóculos",
    ),
    (
        re.compile(r"\brollo de flóculos?\b", re.I),
        "arrastre ascendente de flóculos",
    ),
    (
        re.compile(r"\brollup del flóculo\b", re.I),
        "arrastre ascendente del flóculo",
    ),
    (
        re.compile(r"\brollup de floc\b", re.I),
        "arrastre ascendente de flóculos",
    ),
    (re.compile(r"\bfloc rollup\b", re.I), "arrastre ascendente de flóculos"),
    (
        re.compile(r"\bno enrollándose hacia arriba\b", re.I),
        "sin ser arrastrado hacia arriba",
    ),
    (
        re.compile(r"\bse enrollen\b", re.I),
        "sean arrastrados hacia arriba",
    ),
    (
        re.compile(r"\bse enrollarían los flóculos\b", re.I),
        "serían arrastrados los flóculos hacia arriba",
    ),
    (
        re.compile(r"\bminimizar el enrollamiento\b", re.I),
        "minimizar el arrastre ascendente de flóculos",
    ),
    (
        re.compile(r"\brestricciones por obstrucción y acumulación de flóculos\b", re.I),
        "restricciones por obstrucción y arrastre ascendente de flóculos",
    ),
    (re.compile(r"\blas flóculos\b", re.I), "los flóculos"),
    (re.compile(r"\bdel floc\b", re.I), "del flóculo"),
    (re.compile(r"\bel floc\b", re.I), "el flóculo"),
    (
        re.compile(r"\b(?:asentadores|sedimentadores|estabilizadores) de placas\b", re.I),
        "placas sedimentadoras",
    ),
    (
        re.compile(r"\b(?:asentador|sedimentador|estabilizador) de placas\b", re.I),
        "placa sedimentadora",
    ),
    (re.compile(r"\bla filtro\b", re.I), "el filtro"),
    (re.compile(r"\bel pérdida\b", re.I), "la pérdida"),
    (re.compile(r"\bla nivel\b", re.I), "el nivel"),
    (re.compile(r"\bla agua\b", re.I), "el agua"),
    (re.compile(r"\bde el filtro\b", re.I), "del filtro"),
    (re.compile(r"\ba el filtro\b", re.I), "al filtro"),
    (re.compile(r"\ba lo largo de el\b", re.I), "a lo largo del"),
    (re.compile(r"\bla manifold\b", re.I), "el manifold"),
    (re.compile(r"\bla tanque\b", re.I), "el tanque"),
    (re.compile(r"\bla gradiente\b", re.I), "el gradiente"),
    (re.compile(r"\bla tiempo\b", re.I), "el tiempo"),
    (re.compile(r"\bla flujo\b", re.I), "el flujo"),
    (re.compile(r"\bla canal\b", re.I), "el canal"),
    (re.compile(r"\bla proceso\b", re.I), "el proceso"),
    (re.compile(r"\bla sistema\b", re.I), "el sistema"),
    (re.compile(r"\bla lavado\b", re.I), "el lavado"),
    (re.compile(r"\blos partículas\b", re.I), "las partículas"),
    (re.compile(r"\blas filtros\b", re.I), "los filtros"),
    (re.compile(r"\blas tanques\b", re.I), "los tanques"),
    (re.compile(r"\blas procesos\b", re.I), "los procesos"),
    (re.compile(r"\bun partícula\b", re.I), "una partícula"),
    (re.compile(r"\bun turbidez\b", re.I), "una turbidez"),
    (re.compile(r"\bun velocidad\b", re.I), "una velocidad"),
    (re.compile(r"\bun concentración\b", re.I), "una concentración"),
    (re.compile(r"\bun energía\b", re.I), "una energía"),
    (re.compile(r"\bun geometría\b", re.I), "una geometría"),
    (re.compile(r"\buna flóculo\b", re.I), "un flóculo"),
    (re.compile(r"\buna filtro\b", re.I), "un filtro"),
    (re.compile(r"\buna tanque\b", re.I), "un tanque"),
    (re.compile(r"\buna proceso\b", re.I), "un proceso"),
    (re.compile(r"\buna sistema\b", re.I), "un sistema"),
    (re.compile(r"\buna manifold\b", re.I), "un manifold"),
    (re.compile(r"\bcada uno de las\b", re.I), "cada una de las"),
    (re.compile(r"\btodas los flóculos\b", re.I), "todos los flóculos"),
    (re.compile(r"\bflóculos sedimentadas\b", re.I), "flóculos sedimentados"),
    (re.compile(r"\bse asentarían\b", re.I), "se sedimentarían"),
    (re.compile(r"\bel mismo sedimentación\b", re.I), "la misma sedimentación"),
    (re.compile(r"\bel sedimentación\b", re.I), "la sedimentación"),
    (re.compile(r"\blos placas sedimentadoras\b", re.I), "las placas sedimentadoras"),
    (
        re.compile(r"\bentre los placa sedimentadora\b", re.I),
        "entre las placas sedimentadoras",
    ),
    (re.compile(r"\bun placa sedimentadora\b", re.I), "una placa sedimentadora"),
    (re.compile(r"\bdel placa sedimentadora\b", re.I), "de la placa sedimentadora"),
    (re.compile(r"\bal placa sedimentadora\b", re.I), "a la placa sedimentadora"),
    (re.compile(r"\bel placa sedimentadora\b", re.I), "la placa sedimentadora"),
    (
        re.compile(r"\bplacas sedimentadoras más cercanos\b", re.I),
        "placas sedimentadoras más cercanas",
    ),
    (
        re.compile(r"\b(?:espaciamiento de |espaciamiento )placa sedimentadora\b", re.I),
        "espaciamiento entre placas sedimentadoras",
    ),
    (
        re.compile(r"\bgeometría placa sedimentadora\b", re.I),
        "geometría de las placas sedimentadoras",
    ),
    (
        re.compile(r"\beficiencia placa sedimentadora\b", re.I),
        "eficiencia de las placas sedimentadoras",
    ),
    (
        re.compile(r"\bplacas sedimentadoras realmente compactos\b", re.I),
        "placas sedimentadoras realmente compactas",
    ),
    (re.compile(r"\bturbidez agua\b", re.I), "turbidez del agua"),
    (re.compile(r"\bcalidad agua\b", re.I), "calidad del agua"),
    (re.compile(r"\btanque carga constante\b", re.I), "tanque de carga constante"),
    (
        re.compile(r"\bconsumo de tratamiento de agua\b", re.I),
        "tratamiento de agua potable",
    ),
    (
        re.compile(r"\btratamiento de agua de consumo\b", re.I),
        "tratamiento de agua potable",
    ),
    (re.compile(r"\bagua de beber\b", re.I), "agua potable"),
    (re.compile(r"\basentamientos\b", re.I), "sedimentaciones"),
    (re.compile(r"\basentamiento\b", re.I), "sedimentación"),
    (re.compile(r"\basentarse\b", re.I), "sedimentarse"),
    (re.compile(r"\bse asientan\b", re.I), "se sedimentan"),
    (re.compile(r"\bse asiente\b", re.I), "se sedimente"),
    (re.compile(r"\bdecantar flóculos\b", re.I), "sedimentar flóculos"),
    (re.compile(r"\bmuñones\b", re.I), "niples"),
    (re.compile(r"\bmuñón\b", re.I), "niple"),
    (re.compile(r"\bcontralavados\b", re.I), "retrolavados"),
    (re.compile(r"\bcontralavado\b", re.I), "retrolavado"),
    (re.compile(r"\bcontralavar\b", re.I), "retrolavar"),
    (re.compile(r"\bfiltro de flóculo\b", re.I), "filtro de flóculos"),
    (re.compile(r"\bfiltros flóculos\b", re.I), "filtros de flóculos"),
    (re.compile(r"\bel tolva de lodos\b", re.I), "la tolva de lodos"),
    (re.compile(r"\bun tolva de lodos\b", re.I), "una tolva de lodos"),
    (re.compile(r"\blos tolva de lodos\b", re.I), "las tolvas de lodos"),
    (
        re.compile(r"\btolvas? de flóculos?\b", re.I),
        "tolva de lodos",
    ),
    (
        re.compile(r"\b(?:colector influyente|colector influente|colector de influencia)\b", re.I),
        "manifold de entrada",
    ),
    (re.compile(r"\bmúltiple influente\b", re.I), "manifold de entrada"),
    (re.compile(r"\bcolectores influentes\b", re.I), "manifolds de entrada"),
    (re.compile(r"\bvariedad de influencia\b", re.I), "manifold de entrada"),
    (re.compile(r"\borificio influyente\b", re.I), "orificio de entrada"),
    (re.compile(r"\btubería influyente\b", re.I), "tubería de entrada"),
    (re.compile(r"\btuberías influyentes\b", re.I), "tuberías de entrada"),
    (re.compile(r"\bagua influyente\b", re.I), "agua influente"),
    (re.compile(r"\bturbidez influyente\b", re.I), "turbidez del influente"),
    (
        re.compile(r"\bconcentraciones influyentes\b", re.I),
        "concentraciones del influente",
    ),
    (
        re.compile(r"\bconcentración influyente\b", re.I),
        "concentración del influente",
    ),
    (
        re.compile(r"\bcalidad del agua influyente\b", re.I),
        "calidad del agua influente",
    ),
    (
        re.compile(r"\bagua sedimentada turbidez\b", re.I),
        "turbidez del agua sedimentada",
    ),
    (
        re.compile(r"\bagua clarificada turbidez\b", re.I),
        "turbidez del agua clarificada",
    ),
    (re.compile(r"\bafluentes\b", re.I), "influentes"),
    (re.compile(r"\bafluente\b", re.I), "influente"),
    (re.compile(r"\binfluyentes\b", re.I), "influentes"),
    (re.compile(r"\binfluyente\b", re.I), "influente"),
    (re.compile(r"\binfluents\b", re.I), "influentes"),
    (
        re.compile(r"\bplaca sedimentadora captura de partículas\b", re.I),
        "captura de partículas mediante placas sedimentadoras",
    ),
    (
        re.compile(r"\btolva de lodos consolidación\b", re.I),
        "consolidación en la tolva de lodos",
    ),
    (re.compile(r"\bpartículas agua cruda\b", re.I), "partículas del agua cruda"),
    (
        re.compile(r"\bflocadores floculadores\b", re.I),
        "flóculos del floculador",
    ),
    (
        re.compile(r"\blos suministros de manifold de entrada\b", re.I),
        "el manifold de entrada suministra",
    ),
    (
        re.compile(r"\ben una `de avalancha \(véase\b", re.I),
        "en una avalancha (`véase",
    ),
    (re.compile(r"\befluente clarificador\b", re.I), "efluente del clarificador"),
    (
        re.compile(r"\brendimiento de un clarificante\b", re.I),
        "rendimiento de un clarificador",
    ),
    (
        re.compile(r"\bformación exitosa de filtro de flóculos\b", re.I),
        "formación correcta del filtro de flóculos",
    ),
    (
        re.compile(r"\borificio de entrada del múltiple\b", re.I),
        "orificio del manifold de entrada",
    ),
    (
        re.compile(r"\bno pasaron por coagulación y floculación exitosas\b", re.I),
        "no pasó por una coagulación y una floculación eficaces",
    ),
    (
        re.compile(r"\bno se permitirá la sedimentación de tiempo\b", re.I),
        "no sedimentarán por mucho tiempo que transcurra",
    ),
    (re.compile(r"\bcélula de arcilla\b", re.I), "partícula de arcilla"),
    (
        re.compile(r"\bpuerto influente del varietor\b", re.I),
        "puerto del manifold de entrada",
    ),
    (
        re.compile(r"\btrayectorias influentes de flujo de varietas y difusores\b", re.I),
        "trayectorias de flujo del manifold de entrada y de los difusores",
    ),
    (re.compile(r"\bsistema de variedades\b", re.I), "sistema de manifolds"),
    (
        re.compile(r"\bsalida de la variedad pérdida de carga\b", re.I),
        "pérdida de carga a la salida del manifold",
    ),
    (re.compile(r"\bfiltros de floculación\b", re.I), "filtros de flóculos"),
    (
        re.compile(r"\bevitar romper los floculadores\b", re.I),
        "evitar romper los flóculos",
    ),
    (
        re.compile(r"\bzona de placa sedimentadora activa\b", re.I),
        "zona activa de las placas sedimentadoras",
    ),
    (
        re.compile(r"\brendimiento placa sedimentadora\b", re.I),
        "rendimiento de las placas sedimentadoras",
    ),
    (
        re.compile(r"\bvelocidad de filtro de flóculos de flujo ascendente\b", re.I),
        "velocidad ascendente en el filtro de flóculos",
    ),
    (
        re.compile(r"\bvelocidad de filtro de flóculos\b", re.I),
        "velocidad del filtro de flóculos",
    ),
    (
        re.compile(r"\bvelocidad de captura placa sedimentadora\b", re.I),
        "velocidad de captura de las placas sedimentadoras",
    ),
    (
        re.compile(r"\bdiseño placa sedimentadora\b", re.I),
        "diseño de las placas sedimentadoras",
    ),
    (
        re.compile(r"\befluentes agua filtrada\b", re.I),
        "efluente de agua filtrada",
    ),
    (re.compile(r"\bel agua cruda caudal\b", re.I), "el caudal de agua cruda"),
    (re.compile(r"\bmezcla rápida procesos\b", re.I), "procesos de mezcla rápida"),
    (re.compile(r"\bunidades mezcla rápida\b", re.I), "unidades de mezcla rápida"),
    (re.compile(r"\bunidad mezcla rápida\b", re.I), "unidad de mezcla rápida"),
    (re.compile(r"\bhélice mezcla rápida\b", re.I), "hélice de mezcla rápida"),
    (
        re.compile(r"\bcalidad del agua Ingeniería\b", re.I),
        "Ingeniería de la calidad del agua",
    ),
    (re.compile(r"\bdesperfección de flóculos\b", re.I), "purga de flóculos"),
    (re.compile(r"\bdesgaste de flóculos\b", re.I), "purga de flóculos"),
    (
        re.compile(r"\bel agua clarificada la turbidez\b", re.I),
        "la turbidez del agua clarificada",
    ),
    (
        re.compile(
            r"\(`véase la animación de agregación de flóculos en una placa "
            r"sedimentadora\) <https://youtu\.be/jCjKz6bCD7Y>`_",
            re.I,
        ),
        "`véase la animación de agregación de flóculos en una placa "
        "sedimentadora <https://youtu.be/jCjKz6bCD7Y>`_",
    ),
    (
        re.compile(r"\bdebido a las fuerzas gravitatorias que los tiran hacia abajo\b", re.I),
        "por efecto de la gravedad",
    ),
    (
        re.compile(r"\bsi se dejan el tiempo suficiente\b", re.I),
        "si se deja transcurrir suficiente tiempo",
    ),
    (
        re.compile(r"\bno se permitirá la sedimentación de tiempo\b", re.I),
        "no sedimentarán por mucho tiempo que transcurra",
    ),
    (
        re.compile(r"\beliminación exitosa de partículas\b", re.I),
        "eliminación eficaz de partículas",
    ),
    (
        re.compile(r"\bse estableció por caudal y el área\b", re.I),
        "estaba determinada por el caudal y el área",
    ),
    (
        re.compile(r"\bcambian los parámetros de diseño importantes\b", re.I),
        "cambia el parámetro de diseño principal",
    ),
    (
        re.compile(r"\bmejorar el rendimiento e impactar la velocidad de captura\b", re.I),
        "mejorar el rendimiento y modificar la velocidad de captura",
    ),
    (
        re.compile(r"\bmantener una huella pequeña\b", re.I),
        "mantener una superficie en planta reducida",
    ),
    (
        re.compile(r"\basentadores de lamelas, o lamelas\b", re.I),
        "sedimentadores lamelares o láminas",
    ),
    (
        re.compile(r"\beficiencia de las placas sedimentadoras óptima\b", re.I),
        "eficiencia óptima de las placas sedimentadoras",
    ),
    (
        re.compile(r"\ben el diseño de placa sedimentadora\b", re.I),
        "en el diseño de las placas sedimentadoras",
    ),
    (
        re.compile(r"\bhasta dónde podemos llegar a esto\b", re.I),
        "hasta dónde podemos llevar esta relación",
    ),
    (
        re.compile(r"\btras determinar pérdida de carga\b", re.I),
        "tras determinar la pérdida de carga",
    ),
    (
        re.compile(r"\bno proporcionan mucho pérdida de carga\b", re.I),
        "no generan mucha pérdida de carga",
    ),
    (
        re.compile(
            r"\bpérdida de carga placas sedimentadoras pasantes son realmente pequeños\b",
            re.I,
        ),
        "la pérdida de carga a través de las placas sedimentadoras es realmente pequeña",
    ),
    (
        re.compile(
            r"\ben una avalancha `véase la animación de agregación de flóculos en "
            r"una placa sedimentadora <https://youtu\.be/jCjKz6bCD7Y>`_\.",
            re.I,
        ),
        "en una avalancha (`véase la animación de agregación de flóculos en una "
        "placa sedimentadora <https://youtu.be/jCjKz6bCD7Y>`_).",
    ),
    (re.compile(r"\bcuenca clarificadora\b", re.I), "tanque del clarificador"),
    (
        re.compile(r"\bfuncionamiento exitoso de una planta\b", re.I),
        "funcionamiento correcto de una planta",
    ),
    (re.compile(r"\bclarificación exitosa\b", re.I), "clarificación eficaz"),
    (
        re.compile(r"\bse depositan del agua\b", re.I),
        "se separan del agua por sedimentación",
    ),
    (
        re.compile(r"\bgrandes como para depositarse en el clarificador\b", re.I),
        "grandes como para sedimentarse en el clarificador",
    ),
    (re.compile(r"\bfondo del tarro\b", re.I), "fondo del frasco"),
    (re.compile(r"\bla jarra representa\b", re.I), "el frasco representa"),
    (re.compile(r"\bparte superior del tarro\b", re.I), "parte superior del frasco"),
    (
        re.compile(r"\bsalen del colector\b", re.I),
        "salen del manifold de entrada",
    ),
    (
        re.compile(r"\bdentro del colector da lugar\b", re.I),
        "dentro del manifold da lugar",
    ),
    (re.compile(r"\bextremo terminal del múltiple\b", re.I), "extremo del manifold"),
    (
        re.compile(r"\bclarificadores verticales de flujo\b", re.I),
        "clarificadores de flujo vertical",
    ),
    (
        re.compile(r"\bdifusores de rectificación de flujo\b", re.I),
        "difusores de enderezamiento de flujo",
    ),
    (
        re.compile(r"\. la pérdida de carga a través de las placas\b", re.I),
        ". La pérdida de carga a través de las placas",
    ),
    (
        re.compile(
            r"\bluego se usan filtro de flóculos sedimentación lamelar y filtración por arena\b",
            re.I,
        ),
        "luego se usan el filtro de flóculos, la sedimentación lamelar y la "
        "filtración en arena",
    ),
    (re.compile(r"\bver película en\b", re.I), "véase el video en"),
    (re.compile(r"\bpartículas en bruto\b", re.I), "partículas del agua cruda"),
    (re.compile(r"\bal agua sucia\b", re.I), "al agua cruda"),
    (re.compile(r"\bsin generar tanto cizalladura\b", re.I), "sin generar tanta cizalladura"),
    (re.compile(r"\bque los flóculos se desgarran\b", re.I), "que los flóculos se rompan"),
    (
        re.compile(r"\bo incluso dentro del radio de partículas de arcilla\b", re.I),
        "ni siquiera a una distancia equivalente al radio de una partícula de arcilla",
    ),
    (re.compile(r"\bescala de longitud viscosa interior\b", re.I), "escala de longitud viscosa interna"),
    (re.compile(r"\bfloculaciones hidráulicas\b", re.I), "floculación hidráulica"),
    (
        re.compile(r"\bConsulte el siguiente artículo y libro respectivamente\b"),
        "Consulta el siguiente artículo y el libro, respectivamente",
    ),
    (
        re.compile(r"\bdepende de la ranura con la relación\b", re.I),
        "depende de la relación de ancho de ranura",
    ),
    (re.compile(r"\bcasi ningún pérdida de carga\b", re.I), "casi ninguna pérdida de carga"),
    (
        re.compile(r"\bla parte superior e inferior del floculador serán\b", re.I),
        "las partes superior e inferior del floculador serían",
    ),
    (
        re.compile(r"\bdeberían tener al menos el doble de la relación\b", re.I),
        "debería ser al menos el doble de la relación",
    ),
    (
        re.compile(r"\bque el flujo no se provoque un cortocircuito\b", re.I),
        "que no se produzca un cortocircuito hidráulico",
    ),
    (
        re.compile(r"\bcoeficiente de pérdida de baffle\b", re.I),
        "coeficiente de pérdida del deflector",
    ),
    (
        re.compile(r"\btratamiento de agua de superficie\b", re.I),
        "tratamiento de aguas superficiales",
    ),
    (re.compile(r"\bextensas obras de tierra\b", re.I), "grandes movimientos de tierra"),
    (re.compile(r"\bcrecimiento molesto de algas\b", re.I), "crecimiento indeseado de algas"),
    (
        re.compile(r"\bBeneficios adicionales de la filtración con medios dobles\b"),
        "Los beneficios adicionales de la filtración con medio dual",
    ),
    (re.compile(r"\bfiltración de medio simple y dual\b", re.I), "filtración con uno y dos medios"),
    (re.compile(r"\bfiltración con medio dual\b", re.I), "filtración con dos medios"),
    (
        re.compile(r"\btasa de aumento de pérdida de carga\b", re.I),
        "tasa de aumento de la pérdida de carga",
    ),
    (re.compile(r"\bmedio más grande de los dos\b", re.I), "medio de mayor tamaño de los dos"),
    (re.compile(r"\bese agua\b", re.I), "esa agua"),
    (re.compile(r"\bpozo claro\b", re.I), "depósito de agua filtrada"),
    (re.compile(r"\bla cabeza de la planta\b", re.I), "la cabecera de la planta"),
    (re.compile(r"\bsi pierden potencia\b", re.I), "si pierden el suministro eléctrico"),
    (
        re.compile(r"\bla primera operación en arranque rápido filtro de arena\b", re.I),
        "la primera operación al poner en marcha un filtro rápido de arena",
    ),
    (
        re.compile(r"`<http://cepis\.org\.pe/sobre-el-cepis/>`CEPIS _"),
        "`CEPIS <http://cepis.org.pe/sobre-el-cepis/>`_",
    ),
    (re.compile(r"\brequisito de 6 filtros es gravoso\b", re.I), "requisito de seis filtros es oneroso"),
    (
        re.compile(r"\bLos filtros de arena rápida apilada, StaRS,"),
        "Los filtros rápidos de arena de múltiples capas (FRAMCA; StaRS en inglés)",
    ),
    (re.compile(r"\bLos filtros StaRS utilizan\b", re.I), "Los FRAMCA utilizan"),
    (
        re.compile(r"\bretrolavado Y no requiriera\b"),
        "retrolavado y no requiriera",
    ),
    (
        re.compile(r"\btanto para los modos de retrolavado como para filtración\b", re.I),
        "tanto en modo de retrolavado como de filtración",
    ),
    (re.compile(r"\bya hablaré de eso\b", re.I), "esto se explica más adelante"),
    (re.compile(r"\bAgua Clara\b"), "AguaClara"),
    (re.compile(r"\bespacio de esporas\b", re.I), "espacio poroso"),
    (re.compile(r"\bporosidad total a granel\b", re.I), "porosidad total del lecho"),
    (re.compile(r"\bUn gran :math:`UC = 1`"), "Un valor alto de :math:`UC`"),
    (re.compile(r"\bUn gran :math:`UC`"), "Un valor alto de :math:`UC`"),
    (
        re.compile(r"\bdesarrollo más rápido de pérdida de carga\b", re.I),
        "aumento más rápido de la pérdida de carga",
    ),
    (re.compile(r"\blecho de arena sedimentado\b", re.I), "lecho de arena no expandido"),
    (
        re.compile(
            r"\bEstar parcialmente cubierta por nanopartículas coagulantes permite que "
            r"las partículas del agua cruda colisionen, se adhieran y crezcan\b"
        ),
        "Al estar parcialmente cubiertas por nanopartículas coagulantes, las "
        "partículas del agua cruda pueden colisionar, adherirse y crecer",
    ),
    (
        re.compile(r"\brespectivamente para más datos\b", re.I),
        "respectivamente, para obtener más datos",
    ),
    (
        re.compile(r"\bclarificador con gran ayuda de los floculadores\b", re.I),
        "clarificador, con una contribución importante de los floculadores",
    ),
    (
        re.compile(r"\bla posibilidad de que puedan contener una masa mayor\b", re.I),
        "la posibilidad de que los filtros puedan retener una masa mayor",
    ),
    (re.compile(r"\bluego se desperdicia o se regresa\b", re.I), "luego se descarga o se devuelve"),
    (
        re.compile(r"`_ Este sistema es una solución elegante"),
        "`_. Este sistema es una solución elegante",
    ),
    (
        re.compile(r"\bLos filtros StaRS tienen dos configuraciones\b"),
        "Los FRAMCA se fabrican en dos configuraciones",
    ),
    (
        re.compile(r"\bLos FRAMCA se utilizan para caudales superiores\b"),
        "Los FRAMCA convencionales se utilizan para caudales superiores",
    ),
    (
        re.compile(r"\blos filtros StaRS cerrados \(EStaRS\)", re.I),
        "los FRAMCA cerrados (EStaRS)",
    ),
    (
        re.compile(r"\bpara beber tratamiento de agua\b", re.I),
        "para el tratamiento de agua potable",
    ),
    (
        re.compile(r'In the "worst case scenario", how far'),
        "En el «peor de los casos», ¿qué distancia",
    ),
    (
        re.compile(r"AguaClara design process"),
        "proceso de diseño de AguaClara",
    ),
    (
        re.compile(r"\bintroducirse a estas ideas\b", re.I),
        "presentar estas ideas",
    ),
    (
        re.compile(r"Surface tratamiento de agua for Communities in Developing Countries"),
        "Surface Water Treatment for Communities in Developing Countries",
    ),
    (
        re.compile(r"\blas placas sedimentadoras pérdida de carga muy bajos sugieren\b", re.I),
        "la pérdida de carga muy baja a través de las placas sedimentadoras sugiere",
    ),
    (
        re.compile(r"See this Colab worksheet for determining the filter width for a specific flow rate"),
        "Consulta esta hoja de cálculo de Colab para determinar el ancho del filtro para un caudal específico",
    ),
    (
        re.compile(
            r"Longitud floculadora, :math:`L_\{channel\}`{2} must meet two constraints:.*?"
            r"\*smaller\*\*\*\.",
            re.S,
        ),
        "La longitud del floculador, :math:`L_{channel}`, debe cumplir dos "
        "restricciones: debe ser menor o igual que la longitud de los "
        "clarificadores, ya que el floculador está junto al clarificador. Esta "
        "restricción es :math:`L_{max, \\, sed}`. Además, el floculador debe ser "
        "lo suficientemente corto para alcanzar el volumen objetivo y, al mismo "
        "tiempo, permitir que una persona quepa en su interior, "
        ":math:`L_{max, \\, \\forall}`. **La restricción determinante es la que "
        "produce la longitud *menor***.",
    ),
    (
        re.compile(r":ref:`which is derived in <title_Flocculation_Derivations>`"),
        ":ref:`cuya derivación se presenta aquí <title_Flocculation_Derivations>`",
    ),
    (
        re.compile(
            r"Muchas de las ecuaciones fractales de flóculo están disponibles en el "
            r"``floc_model\.py`` file in the aguaclara repository\..*?requiere 'coag' "
            r"como entrada\.",
            re.S,
        ),
        "Muchas de las ecuaciones de flóculos fractales están disponibles en el "
        "archivo ``floc_model.py`` del repositorio aguaclara. Consulta "
        "```floc_model.py`` <https://github.com/AguaClara/aguaclara/blob/master/"
        "aguaclara/research/floc_model.py>`_. En ese archivo se definen las "
        "siguientes constantes. La relación empírica aproximada entre la "
        "concentración de arcilla de caolín y la turbidez establece que 1 NTU "
        "equivale a 1,7 mg/L. Se supone que el diámetro de una partícula primaria "
        "de arcilla es de 7 micrómetros. La dimensión fractal de los flóculos se "
        "define como ``DIM_FRACTAL`` y es igual a 2,1. En este análisis usamos PACl "
        "como coagulante; por tanto, usa ``fm.PACl`` cuando una función de "
        "``floc_model.py`` requiera ``coag`` como entrada.",
    ),
    (
        re.compile(
            r"Volvamos al ámbito de la tratamiento de agua\..*?specifically in the "
            r"laminar region\.",
            re.S,
        ),
        "Volvamos al ámbito del tratamiento de agua. Los coeficientes de arrastre "
        "y las velocidades terminales permiten describir cómo se mueven los "
        "flóculos en el agua. Los flóculos suelen encontrarse en la región "
        "1 < :math:`Re` < 10. La ley de Stokes no describe perfectamente esta "
        "región, pero puede usarse como una aproximación adecuada. Ya obtuvimos la "
        "ecuación general de la velocidad terminal mediante un balance de fuerzas. "
        "Ahora podemos obtener una ecuación de velocidad terminal específica para "
        "la región laminar.",
    ),
    (
        re.compile(r"hoja de cálculo Flóculos, Fractales and Forces Colab para estimar la fuerza de unión"),
        "hoja de cálculo de Colab para estimar la fuerza de unión en Flóculos, Fractales y Fuerzas",
    ),
    (re.compile(r"the Sutro Weir"), "el vertedero Sutro"),
    (re.compile(r"\bel mezcla rápida orificio\b", re.I), "el orificio de mezcla rápida"),
    (re.compile(r"In the case of a `rectangular weir"), "En el caso de un `vertedero rectangular"),
    (re.compile(r"`v-notch weir"), "`vertedero de escotadura en V"),
    (re.compile(r"`Sutro weir"), "`vertedero Sutro"),
    (re.compile(r"linear flow orifice meter"), "medidor de orificio de flujo lineal"),
    (re.compile(r"Colab worksheet to plot the shaft power"), "Hoja de cálculo de Colab para graficar la potencia del eje"),
    (re.compile(r"\*no viscosity\*"), "*viscosidad nula*"),
    (re.compile(r"See this textbook"), "Consulta este libro de texto"),
    (
        re.compile(r"\*\*Orifice equation and vena contractas:\*\*"),
        "**Ecuación del orificio y vena contracta:**",
    ),
    (re.compile(r"\bpara el flow\b", re.I), "para el flujo"),
    (re.compile(r"\btable below\b"), "tabla siguiente"),
    (
        re.compile(r"access and modify the models is given below the table"),
        "acceder a los modelos y modificarlos se presenta debajo de la tabla",
    ),
    (
        re.compile(r"encuesta de `sobre posibles socios de implementación"),
        "`encuesta para posibles socios de implementación",
    ),
    (
        re.compile(
            r"< The change in thickness of the jet after the 180 degree bend is due "
            r"to the flow spreading out to fill in the gaps created by the diffuser "
            r"pipe walls\."
        ),
        " El cambio de espesor del chorro después del giro de 180 grados se debe a "
        "que el flujo se extiende para llenar los espacios creados por las paredes "
        "de las tuberías difusoras.",
    ),
    (re.compile(r"\berosión por aire\b", re.I), "lavado con aire"),
    (re.compile(r"\bcuando la mayoría se contrae\b", re.I), "en la contracción máxima"),
    (re.compile(r"37\.3%"), "37,3 %"),
    (re.compile(r"la `:ref:`tercera forma"), "la :ref:`tercera forma"),
    (
        re.compile(r"` and its definition of the minor loss coefficient,"),
        "` y su definición del coeficiente de pérdida menor,",
    ),
    (re.compile(r"\\derecha"), r"\right"),
    (re.compile(r"\\izquierda"), r"\left"),
    (
        re.compile(r"\bla pérdida de carga observado era mayor\b", re.I),
        "la pérdida de carga observada era mayor",
    ),
    (
        re.compile(r"`A paper by Haarhoff and van der Walt in 2001"),
        "`Un artículo de Haarhoff y van der Walt de 2001",
    ),
    (re.compile(r"\bpara asegurarnos :math:"), "para asegurarnos de que :math:"),
    (re.compile(r"\bremuíños\b", re.I), "remolinos"),
    (
        re.compile(r"tiempo de recambio del remolino `<http"),
        "`tiempo de recambio del remolino <http",
    ),
    (
        re.compile(r"The derivation for the equation below is found here"),
        "La derivación de la ecuación siguiente se encuentra aquí",
    ),
    (re.compile(r"\btruco pérdida de carga\b", re.I), "truco de la pérdida de carga"),
    (re.compile(r"\*into\*"), "en"),
    (re.compile(r"\bun recipiente un recipiente\b", re.I), "un recipiente"),
    (re.compile(r"\bagua potable segura\b", re.I), "agua potable"),
    (
        re.compile(r"```floc_model\.py`` <https://github\.com/AguaClara/aguaclara/blob/master/aguaclara/research/floc_model\.py>`_"),
        "`floc_model.py <https://github.com/AguaClara/aguaclara/blob/master/aguaclara/research/floc_model.py>`_",
    ),
    (
        re.compile(r"\bse envuelven en la siguiente ecuación\b", re.I),
        "se combinan en la siguiente ecuación",
    ),
    (
        re.compile(r"\brestricción del arrastre ascendente de flóculos\b", re.I),
        "restricción por arrastre ascendente de flóculos",
    ),
    (
        re.compile(r"\brestricciones de obstrucción y arrastre ascendente de flóculos\b", re.I),
        "restricciones por obstrucción y arrastre ascendente de flóculos",
    ),
    (
        re.compile(r"\bEl arrastre ascendente de flóculos en función de la densidad y las temperaturas de partículas del núcleo\b", re.I),
        "Arrastre ascendente de flóculos en función de la densidad de las partículas primarias y la temperatura",
    ),
    (
        re.compile(r"\bComo se ha discutido, (:ref:`arrastre ascendente de flóculos <heading_Floc_Rollup>`) es un modo de fallo de rendimiento de las placas sedimentadoras\. Para determinar el espaciamiento adecuado entre las placas sedimentadoras, debemos considerar el potencial de que los flóculos sean arrastrados hacia arriba porque queremos minimizar el arrastre ascendente de flóculos y promover la sedimentación\.", re.I),
        "Como se explicó, :ref:`arrastre ascendente de flóculos "
        "<heading_Floc_Rollup>` es un modo de falla del funcionamiento de las "
        "placas sedimentadoras. Para determinar el espaciamiento adecuado entre "
        "las placas sedimentadoras, debemos considerar la posibilidad de que los "
        "flóculos sean arrastrados hacia arriba; el objetivo es minimizar este "
        "arrastre y favorecer la sedimentación.",
    ),
    (
        re.compile(r"Como se explicó, \\1 es un modo de falla"),
        "Como se explicó, :ref:`arrastre ascendente de flóculos "
        "<heading_Floc_Rollup>` es un modo de falla",
    ),
    (
        re.compile(r"\baunque los flóculos se asienten sobre la placa\b", re.I),
        "aunque los flóculos se sedimenten sobre la placa",
    ),
    (
        re.compile(r"¿Por qué serían arrastrados los flóculos hacia arriba\?", re.I),
        "¿Por qué se produciría el arrastre ascendente de los flóculos?",
    ),
    (
        re.compile(r"\bHay una fuerza de gravedad que tira de la partícula hacia abajo, equilibrada con la fuerza que ejerce el flujo del fluido a través del arrastre relacionada con la viscosidad\.", re.I),
        "La fuerza de gravedad que hace descender el flóculo se equilibra con la fuerza de arrastre viscoso ejercida por el flujo.",
    ),
    (
        re.compile(r"\bPero, ¿por qué importa si las placas están juntas para el arrastre ascendente de flóculos\?", re.I),
        "Pero ¿por qué influye la separación entre placas en el arrastre ascendente de flóculos?",
    ),
    (
        re.compile(r"\bEn comparación con placas con mayor espaciamiento, las placas más cercanas provocan una mayor velocidad más cercana a la superficie de la placa\.", re.I),
        "En comparación con placas más separadas, las placas próximas producen velocidades mayores cerca de su superficie.",
    ),
    (
        re.compile(r"\bEsto significa que los flóculos entre placas muy cercanas verán una mayor velocidad más cercana a la placa sedimentadora, lo que afectará al equilibrio de fuerzas\.", re.I),
        "Por tanto, los flóculos entre placas muy próximas experimentan una velocidad mayor cerca de la placa sedimentadora, lo que modifica el equilibrio de fuerzas.",
    ),
    (
        re.compile(r"plate settler design"),
        "diseño de las placas sedimentadoras",
    ),
    (
        re.compile(r"¿Serán los flóculos pequeños o grandes los más vulnerables al arrastre ascendente de flóculos\?", re.I),
        "¿Los flóculos pequeños o los grandes serán más vulnerables al arrastre ascendente?",
    ),
    (
        re.compile(r"¿El espaciamiento grande o pequeño entre placas causará más arrastre ascendente de flóculos\?", re.I),
        "¿Un espaciamiento amplio o reducido entre placas causará mayor arrastre ascendente de flóculos?",
    ),
    (
        re.compile(r"\bun pequeño espaciamiento entre placas provocará más arrastre ascendente de flóculos\b", re.I),
        "un espaciamiento reducido entre placas provocará mayor arrastre ascendente de flóculos",
    ),
    (
        re.compile(r"\(haz clic para enviarlo al vídeo\)", re.I),
        "(haz clic para ver el video)",
    ),
    (
        re.compile(r"\bLas placas sedimentadoras de AguaClara están utilizando actualmente separaciones de 2,5 cm, que está muy por encima de la restricción por arrastre ascendente de flóculos salvo para los flóculos de muy baja densidad\. A medida que disminuye la densidad de flóculos, como esperamos para la materia orgánica, el espaciamiento mínimo aumenta\. Sin embargo, aún no sabemos cuál es ese espaciamiento ni dónde está el límite porque no conocemos las propiedades de los flóculos húmico-coagulante\. Se requiere más investigación aquí para determinar las propiedades de los flóculos dominados por materia orgánica disuelta\.", re.I),
        "Las placas sedimentadoras de AguaClara utilizan actualmente un espaciamiento de 2,5 cm, muy superior al mínimo impuesto por la restricción de arrastre ascendente, excepto para flóculos de muy baja densidad. A medida que disminuye la densidad de los flóculos, como cabe esperar cuando contienen materia orgánica, aumenta el espaciamiento mínimo. Sin embargo, aún no conocemos ese espaciamiento ni el límite porque desconocemos las propiedades de los flóculos formados por ácido húmico y coagulante. Se requiere más investigación para determinar las propiedades de los flóculos dominados por materia orgánica disuelta.",
    ),
    (
        re.compile(r"\bLa derivación del balance de fuerzas se encuentra\b", re.I),
        "La derivación del equilibrio de fuerzas se encuentra",
    ),
    (
        re.compile(r"¿Cómo definirías la transición entre el arrastre ascendente del flóculo y el deslizamiento hacia abajo\? ¿Cómo describirías el caso de un flóculo que está fijo en la placa sedimentadora \(sin ser arrastrado hacia arriba ni deslizándose hacia abajo\)\?", re.I),
        "¿Cómo definirías la transición entre el arrastre ascendente y el deslizamiento descendente? ¿Qué condición corresponde a un flóculo inmóvil sobre la placa sedimentadora, sin ser arrastrado hacia arriba ni deslizarse hacia abajo?",
    ),
)


def matching_case(match: re.Match[str], replacement: str) -> str:
    if match.group()[0].isupper():
        return replacement[0].upper() + replacement[1:]
    return replacement


def normalize(value: str) -> str:
    for pattern, replacement in RULES:
        value = pattern.sub(lambda match: matching_case(match, replacement), value)
    return value


def quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def encode_msgstr(value: str, width: int = 70) -> list[str]:
    if len(value) <= width and "\n" not in value:
        return [f"msgstr {quoted(value)}"]
    chunks = [value[index : index + width] for index in range(0, len(value), width)]
    return ['msgstr ""', *(quoted(chunk) for chunk in chunks)]


def normalize_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    changed = 0
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.startswith("msgstr "):
            output.append(line)
            index += 1
            continue

        block = [line.removeprefix("msgstr ")]
        end = index + 1
        while end < len(lines) and lines[end].startswith('"'):
            block.append(lines[end])
            end += 1
        with warnings.catch_warnings():
            # PO strings can contain LaTeX escapes such as ``\,`` that Python
            # preserves correctly but warns about while parsing the literal.
            warnings.simplefilter("ignore", SyntaxWarning)
            value = "".join(ast.literal_eval(part) for part in block)
        normalized = value
        if path.name == "Manifold_Hydraulics.po":
            normalized = re.sub(r"\bvariedades\b", "manifolds", normalized, flags=re.I)
            normalized = re.sub(r"\bvariedad\b", "manifold", normalized, flags=re.I)
        normalized = normalize(normalized)
        if normalized == value:
            output.extend(lines[index:end])
        else:
            output.extend(encode_msgstr(normalized))
            changed += 1
        index = end

    if changed:
        path.write_text("\n".join(output) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "locale_dir",
        nargs="?",
        type=Path,
        default=Path("Textbook/locale/es/LC_MESSAGES"),
    )
    args = parser.parse_args()
    files_changed = 0
    messages_changed = 0
    for path in sorted(args.locale_dir.rglob("*.po")):
        count = normalize_file(path)
        if count:
            files_changed += 1
            messages_changed += count
    print(f"Normalized {messages_changed} messages in {files_changed} catalogs.")


if __name__ == "__main__":
    main()
