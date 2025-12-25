-- Seed data for interests table
-- Run this after creating the interests table

INSERT INTO interests (name, category) VALUES
-- Sports
('football', 'sports'),
('basketball', 'sports'),
('soccer', 'sports'),
('tennis', 'sports'),
('baseball', 'sports'),
('volleyball', 'sports'),
('swimming', 'sports'),
('running', 'sports'),
('cycling', 'sports'),
('yoga', 'sports'),
-- Technology
('software-engineering', 'technology'),
('web-development', 'technology'),
('mobile-development', 'technology'),
('data-science', 'technology'),
('machine-learning', 'technology'),
('product-management', 'technology'),
('ui-ux-design', 'technology'),
('cybersecurity', 'technology'),
('cloud-computing', 'technology'),
('devops', 'technology'),
-- Arts & Creative
('music', 'arts'),
('photography', 'arts'),
('writing', 'arts'),
('painting', 'arts'),
('drawing', 'arts'),
('graphic-design', 'arts'),
('video-editing', 'arts'),
('acting', 'arts'),
('dancing', 'arts'),
('singing', 'arts'),
-- Hobbies & Interests
('cooking', 'hobbies'),
('reading', 'hobbies'),
('gaming', 'hobbies'),
('travel', 'hobbies'),
('hiking', 'hobbies'),
('fitness', 'hobbies'),
('gardening', 'hobbies'),
('knitting', 'hobbies'),
('board-games', 'hobbies'),
('puzzles', 'hobbies'),
-- Career & Business
('entrepreneurship', 'business'),
('finance', 'business'),
('marketing', 'business'),
('sales', 'business'),
('consulting', 'business'),
('investing', 'business'),
('startups', 'business'),
('leadership', 'business'),
-- Other
('volunteering', 'other'),
('mentoring', 'other'),
('public-speaking', 'other'),
('networking', 'other')
ON CONFLICT (name) DO NOTHING;

