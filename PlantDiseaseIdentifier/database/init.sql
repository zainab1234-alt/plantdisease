
CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,
    plant VARCHAR(255) NOT NULL,
    disease VARCHAR(255) NOT NULL,
    symptoms TEXT,
    treatment TEXT
);

INSERT INTO diseases (plant, disease, symptoms, treatment) VALUES
('Tomato', 'Blight', 'Yellowing leaves, black spots', 'Use fungicide, improve air circulation'),
('Potato', 'Scab', 'Rough patches on skin', 'Use resistant varieties, maintain soil pH'),
('Rose', 'Black Spot', 'Black spots on leaves', 'Prune infected leaves, apply fungicide');
