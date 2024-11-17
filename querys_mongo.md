// Contar el número total de documentos en la colección
db.co2_emissions.aggregate([
  { $count: "total_documents" }
]);

// Sumar las emisiones de CO2 (Kilotons of Co2)
db.co2_emissions.aggregate([
  { $group: { _id: null, totalKilotons: { $sum: "$Kilotons of Co2" } } }
]);

// Promediar las emisiones per cápita (Metric Tons Per Capita)
db.co2_emissions.aggregate([
  { $group: { _id: null, avgMetricTonsPerCapita: { $avg: "$Metric Tons Per Capita" } } }
]);

// Calcular el máximo y el mínimo de emisiones de CO2
db.co2_emissions.aggregate([
  { $group: { _id: null, maxKilotons: { $max: "$Kilotons of Co2" }, minKilotons: { $min: "$Kilotons of Co2" } } }
]);

// Contar el número de documentos por región
db.co2_emissions.aggregate([
  { $group: { _id: "$Region", count: { $sum: 1 } } }
]);

// Sumar las emisiones de CO2 por región
db.co2_emissions.aggregate([
  { $group: { _id: "$Region", totalKilotons: { $sum: "$Kilotons of Co2" } } }
]);

// Promediar las emisiones per cápita por país
db.co2_emissions.aggregate([
  { $group: { _id: "$Country", avgMetricTonsPerCapita: { $avg: "$Metric Tons Per Capita" } } }
]);

// Filtrar y sumar las emisiones de CO2 mayores a 8000 por región
db.co2_emissions.aggregate([
  { $match: { "Kilotons of Co2": { $gt: 8000 } } },
  { $group: { _id: "$Region", totalKilotons: { $sum: "$Kilotons of Co2" } } }
]);

// Ordenar las emisiones por región de mayor a menor
db.co2_emissions.aggregate([
  { $group: { _id: "$Region", totalKilotons: { $sum: "$Kilotons of Co2" } } },
  { $sort: { totalKilotons: -1 } }
]);

// Filtrar y agrupar las emisiones per cápita mayores o iguales a 0.2
db.co2_emissions.aggregate([
  { $match: { "Metric Tons Per Capita": { $gte: 0.2 } } },
  { $group: { _id: "$Country", avgMetricTonsPerCapita: { $avg: "$Metric Tons Per Capita" } } }
]);

