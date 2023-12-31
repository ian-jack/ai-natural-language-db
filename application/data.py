load_cow_table = """
    INSERT INTO cow VALUES
    (1, 'Bérangère', 5),
    (2, 'Mahélie', 11),
    (3, 'Cinéma', 2),
    (4, 'Valérie', 8),
    (5, 'Gaëlle', 6),
    (6, 'Camélia', 3),
    (7, 'Eléa', 10),
    (8, 'Chloé', 11),
    (9, 'Naëlle', 7),
    (10, 'Dafnée', 12),
    (11, 'Björn', 3),
    (12, 'Annotés', 16),
    (13, 'Vérane', 0),
    (14, 'Marie-ève', 11),
    (15, 'Gwenaëlle', 2),
    (16, 'Mén', 12),
    (17, 'Illustrée', 5),
    (18, 'Gösta', 2),
    (19, 'Célestine', 16),
    (20, 'Anaé', 9);
"""

load_milk_yield_table = """
    INSERT INTO milk_yield VALUES
    ('1', '8/1/2023', 2.1),
    ('2', '8/1/2023', 4.9),
    ('3', '8/1/2023', 4.7),
    ('4', '8/1/2023', 4.0),
    ('5', '8/1/2023', 4.7),
    ('6', '8/1/2023', 1.8),
    ('7', '8/1/2023', 1.5),
    ('8', '8/1/2023', 2.4),
    ('9', '8/1/2023', 3.3),
    ('10', '8/1/2023', 4.1),
    ('11', '8/1/2023', 1.7),
    ('12', '8/1/2023', 2.9),
    ('13', '8/1/2023', 2.7),
    ('14', '8/1/2023', 4.9),
    ('15', '8/1/2023', 1.1),
    ('16', '8/1/2023', 1.0),
    ('17', '8/1/2023', 3.9),
    ('18', '8/1/2023', 4.0),
    ('19', '8/1/2023', 1.5),
    ('20', '8/1/2023', 2.2),
    ('1', '8/2/2023', 4.7),
    ('2', '8/2/2023', 3.1),
    ('3', '8/2/2023', 3.0),
    ('4', '8/2/2023', 4.6),
    ('5', '8/2/2023', 2.2),
    ('6', '8/2/2023', 3.8),
    ('7', '8/2/2023', 3.3),
    ('8', '8/2/2023', 4.5),
    ('9', '8/2/2023', 1.6),
    ('10', '8/2/2023', 4.9),
    ('11', '8/2/2023', 2.5),
    ('12', '8/2/2023', 1.4),
    ('13', '8/2/2023', 2.3),
    ('14', '8/2/2023', 3.1),
    ('15', '8/2/2023', 2.8),
    ('16', '8/2/2023', 1.1),
    ('17', '8/2/2023', 3.5),
    ('18', '8/2/2023', 2.6),
    ('19', '8/2/2023', 3.9),
    ('20', '8/2/2023', 4.1),
    ('1', '8/3/2023', 2.7),
    ('2', '8/3/2023', 4.8),
    ('3', '8/3/2023', 2.9),
    ('4', '8/3/2023', 4.5),
    ('5', '8/3/2023', 1.3),
    ('6', '8/3/2023', 4.7),
    ('7', '8/3/2023', 2.3),
    ('8', '8/3/2023', 3.1),
    ('9', '8/3/2023', 4.7),
    ('10', '8/3/2023', 1.4),
    ('11', '8/3/2023', 4.3),
    ('12', '8/3/2023', 3.3),
    ('13', '8/3/2023', 1.2),
    ('14', '8/3/2023', 4.8),
    ('15', '8/3/2023', 2.4),
    ('16', '8/3/2023', 3.6),
    ('17', '8/3/2023', 3.1),
    ('18', '8/3/2023', 3.9),
    ('19', '8/3/2023', 2.3),
    ('20', '8/3/2023', 2.6),
    ('1', '8/4/2023', 3.1),
    ('2', '8/4/2023', 3.3),
    ('3', '8/4/2023', 3.2),
    ('4', '8/4/2023', 4.1),
    ('5', '8/4/2023', 1.6),
    ('6', '8/4/2023', 4.7),
    ('7', '8/4/2023', 1.1),
    ('8', '8/4/2023', 1.7),
    ('9', '8/4/2023', 4.2),
    ('10', '8/4/2023', 3.2),
    ('11', '8/4/2023', 4.0),
    ('12', '8/4/2023', 3.6),
    ('13', '8/4/2023', 3.7),
    ('14', '8/4/2023', 3.0),
    ('15', '8/4/2023', 3.7),
    ('16', '8/4/2023', 1.1),
    ('17', '8/4/2023', 3.8),
    ('18', '8/4/2023', 2.0),
    ('19', '8/4/2023', 3.3),
    ('20', '8/4/2023', 4.5),
    ('1', '8/5/2023', 4.9),
    ('2', '8/5/2023', 2.7),
    ('3', '8/5/2023', 1.0),
    ('4', '8/5/2023', 1.8),
    ('5', '8/5/2023', 2.0),
    ('6', '8/5/2023', 3.6),
    ('7', '8/5/2023', 4.4),
    ('8', '8/5/2023', 3.1),
    ('9', '8/5/2023', 3.0),
    ('10', '8/5/2023', 3.0),
    ('11', '8/5/2023', 4.0),
    ('12', '8/5/2023', 3.1),
    ('13', '8/5/2023', 2.3),
    ('14', '8/5/2023', 3.3),
    ('15', '8/5/2023', 2.6),
    ('16', '8/5/2023', 3.3),
    ('17', '8/5/2023', 4.6),
    ('18', '8/5/2023', 4.5),
    ('19', '8/5/2023', 4.9),
    ('20', '8/5/2023', 2.2),
    ('1', '8/6/2023', 4.1),
    ('2', '8/6/2023', 2.9),
    ('3', '8/6/2023', 3.8),
    ('4', '8/6/2023', 3.3),
    ('5', '8/6/2023', 4.8),
    ('6', '8/6/2023', 1.3),
    ('7', '8/6/2023', 3.4),
    ('8', '8/6/2023', 1.0),
    ('9', '8/6/2023', 3.3),
    ('10', '8/6/2023', 4.5),
    ('11', '8/6/2023', 3.0),
    ('12', '8/6/2023', 2.4),
    ('13', '8/6/2023', 2.5),
    ('14', '8/6/2023', 3.9),
    ('15', '8/6/2023', 2.9),
    ('16', '8/6/2023', 1.2),
    ('17', '8/6/2023', 4.4),
    ('18', '8/6/2023', 2.2),
    ('19', '8/6/2023', 4.4),
    ('20', '8/6/2023', 4.5),
    ('1', '8/7/2023', 1.0),
    ('2', '8/7/2023', 2.1),
    ('3', '8/7/2023', 4.7),
    ('4', '8/7/2023', 2.4),
    ('5', '8/7/2023', 2.0),
    ('6', '8/7/2023', 4.6),
    ('7', '8/7/2023', 1.9),
    ('8', '8/7/2023', 2.6),
    ('9', '8/7/2023', 3.5),
    ('10', '8/7/2023', 2.9),
    ('11', '8/7/2023', 4.5),
    ('12', '8/7/2023', 2.5),
    ('13', '8/7/2023', 4.5),
    ('14', '8/7/2023', 2.5),
    ('15', '8/7/2023', 1.8),
    ('16', '8/7/2023', 4.2),
    ('17', '8/7/2023', 2.9),
    ('18', '8/7/2023', 3.1),
    ('19', '8/7/2023', 2.0),
    ('20', '8/7/2023', 2.7),
    ('1', '8/8/2023', 1.9),
    ('2', '8/8/2023', 1.7),
    ('3', '8/8/2023', 4.0),
    ('4', '8/8/2023', 4.2),
    ('5', '8/8/2023', 3.1),
    ('6', '8/8/2023', 4.4),
    ('7', '8/8/2023', 4.6),
    ('8', '8/8/2023', 1.5),
    ('9', '8/8/2023', 2.2),
    ('10', '8/8/2023', 4.1),
    ('11', '8/8/2023', 4.5),
    ('12', '8/8/2023', 1.3),
    ('13', '8/8/2023', 1.3),
    ('14', '8/8/2023', 3.5),
    ('15', '8/8/2023', 1.2),
    ('16', '8/8/2023', 4.5),
    ('17', '8/8/2023', 3.2),
    ('18', '8/8/2023', 3.1),
    ('19', '8/8/2023', 1.7),
    ('20', '8/8/2023', 2.7),
    ('1', '8/9/2023', 1.9),
    ('2', '8/9/2023', 3.7),
    ('3', '8/9/2023', 1.8),
    ('4', '8/9/2023', 4.4),
    ('5', '8/9/2023', 4.0),
    ('6', '8/9/2023', 2.8),
    ('7', '8/9/2023', 3.2),
    ('8', '8/9/2023', 2.7),
    ('9', '8/9/2023', 4.6),
    ('10', '8/9/2023', 3.0),
    ('11', '8/9/2023', 3.2),
    ('12', '8/9/2023', 1.9),
    ('13', '8/9/2023', 2.1),
    ('14', '8/9/2023', 1.7),
    ('15', '8/9/2023', 4.5),
    ('16', '8/9/2023', 4.3),
    ('17', '8/9/2023', 1.2),
    ('18', '8/9/2023', 1.1),
    ('19', '8/9/2023', 1.5),
    ('20', '8/9/2023', 3.4),
    ('1', '8/10/2023', 2.8),
    ('2', '8/10/2023', 2.5),
    ('3', '8/10/2023', 3.5),
    ('4', '8/10/2023', 4.1),
    ('5', '8/10/2023', 2.2),
    ('6', '8/10/2023', 1.1),
    ('7', '8/10/2023', 1.2),
    ('8', '8/10/2023', 3.3),
    ('9', '8/10/2023', 1.7),
    ('10', '8/10/2023', 2.2),
    ('11', '8/10/2023', 2.8),
    ('12', '8/10/2023', 3.3),
    ('13', '8/10/2023', 1.3),
    ('14', '8/10/2023', 1.1),
    ('15', '8/10/2023', 3.1),
    ('16', '8/10/2023', 3.9),
    ('17', '8/10/2023', 4.3),
    ('18', '8/10/2023', 3.4),
    ('19', '8/10/2023', 1.2),
    ('20', '8/10/2023', 3.5),
    ('1', '8/11/2023', 2.1),
    ('2', '8/11/2023', 1.5),
    ('3', '8/11/2023', 1.8),
    ('4', '8/11/2023', 3.6),
    ('5', '8/11/2023', 2.3),
    ('6', '8/11/2023', 4.0),
    ('7', '8/11/2023', 4.4),
    ('8', '8/11/2023', 1.6),
    ('9', '8/11/2023', 1.4),
    ('10', '8/11/2023', 3.6),
    ('11', '8/11/2023', 1.7),
    ('12', '8/11/2023', 2.0),
    ('13', '8/11/2023', 2.3),
    ('14', '8/11/2023', 4.9),
    ('15', '8/11/2023', 4.4),
    ('16', '8/11/2023', 3.3),
    ('17', '8/11/2023', 2.2),
    ('18', '8/11/2023', 5.0),
    ('19', '8/11/2023', 4.4),
    ('20', '8/11/2023', 1.2),
    ('1', '8/12/2023', 4.2),
    ('2', '8/12/2023', 4.9),
    ('3', '8/12/2023', 2.0),
    ('4', '8/12/2023', 1.1),
    ('5', '8/12/2023', 3.7),
    ('6', '8/12/2023', 2.6),
    ('7', '8/12/2023', 2.8),
    ('8', '8/12/2023', 3.3),
    ('9', '8/12/2023', 1.6),
    ('10', '8/12/2023', 4.6),
    ('11', '8/12/2023', 2.5),
    ('12', '8/12/2023', 2.5),
    ('13', '8/12/2023', 1.1),
    ('14', '8/12/2023', 4.5),
    ('15', '8/12/2023', 2.8),
    ('16', '8/12/2023', 1.4),
    ('17', '8/12/2023', 2.4),
    ('18', '8/12/2023', 2.4),
    ('19', '8/12/2023', 3.6),
    ('20', '8/12/2023', 1.1),
    ('1', '8/13/2023', 4.1),
    ('2', '8/13/2023', 1.2),
    ('3', '8/13/2023', 4.6),
    ('4', '8/13/2023', 2.7),
    ('5', '8/13/2023', 1.6),
    ('6', '8/13/2023', 2.1),
    ('7', '8/13/2023', 3.9),
    ('8', '8/13/2023', 4.3),
    ('9', '8/13/2023', 3.1),
    ('10', '8/13/2023', 1.5),
    ('11', '8/13/2023', 4.4),
    ('12', '8/13/2023', 3.0),
    ('13', '8/13/2023', 1.6),
    ('14', '8/13/2023', 1.6),
    ('15', '8/13/2023', 1.3),
    ('16', '8/13/2023', 2.9),
    ('17', '8/13/2023', 3.5),
    ('18', '8/13/2023', 4.7),
    ('19', '8/13/2023', 1.2),
    ('20', '8/13/2023', 4.9),
    ('1', '8/14/2023', 4.3),
    ('2', '8/14/2023', 1.8),
    ('3', '8/14/2023', 2.4),
    ('4', '8/14/2023', 2.0),
    ('5', '8/14/2023', 3.2),
    ('6', '8/14/2023', 1.0),
    ('7', '8/14/2023', 1.3),
    ('8', '8/14/2023', 1.9),
    ('9', '8/14/2023', 4.0),
    ('10', '8/14/2023', 2.3),
    ('11', '8/14/2023', 4.5),
    ('12', '8/14/2023', 1.2),
    ('13', '8/14/2023', 4.0),
    ('14', '8/14/2023', 4.8),
    ('15', '8/14/2023', 3.7),
    ('16', '8/14/2023', 1.2),
    ('17', '8/14/2023', 4.0),
    ('18', '8/14/2023', 3.6),
    ('19', '8/14/2023', 1.8),
    ('20', '8/14/2023', 1.4),
    ('1', '8/15/2023', 1.1),
    ('2', '8/15/2023', 3.1),
    ('3', '8/15/2023', 3.8),
    ('4', '8/15/2023', 2.1),
    ('5', '8/15/2023', 3.7),
    ('6', '8/15/2023', 1.1),
    ('7', '8/15/2023', 4.4),
    ('8', '8/15/2023', 1.3),
    ('9', '8/15/2023', 4.6),
    ('10', '8/15/2023', 1.4),
    ('11', '8/15/2023', 1.1),
    ('12', '8/15/2023', 3.4),
    ('13', '8/15/2023', 3.5),
    ('14', '8/15/2023', 2.2),
    ('15', '8/15/2023', 4.6),
    ('16', '8/15/2023', 3.8),
    ('17', '8/15/2023', 4.0),
    ('18', '8/15/2023', 4.9),
    ('19', '8/15/2023', 2.9),
    ('20', '8/15/2023', 3.5),
    ('1', '8/16/2023', 1.9),
    ('2', '8/16/2023', 2.2),
    ('3', '8/16/2023', 3.2),
    ('4', '8/16/2023', 2.8),
    ('5', '8/16/2023', 3.8),
    ('6', '8/16/2023', 3.3),
    ('7', '8/16/2023', 4.0),
    ('8', '8/16/2023', 4.5),
    ('9', '8/16/2023', 1.7),
    ('10', '8/16/2023', 4.1),
    ('11', '8/16/2023', 1.4),
    ('12', '8/16/2023', 4.6),
    ('13', '8/16/2023', 1.9),
    ('14', '8/16/2023', 3.0),
    ('15', '8/16/2023', 2.0),
    ('16', '8/16/2023', 2.8),
    ('17', '8/16/2023', 1.4),
    ('18', '8/16/2023', 1.6),
    ('19', '8/16/2023', 4.6),
    ('20', '8/16/2023', 4.5),
    ('1', '8/17/2023', 4.0),
    ('2', '8/17/2023', 2.0),
    ('3', '8/17/2023', 4.0),
    ('4', '8/17/2023', 2.4),
    ('5', '8/17/2023', 3.9),
    ('6', '8/17/2023', 5.0),
    ('7', '8/17/2023', 3.3),
    ('8', '8/17/2023', 4.7),
    ('9', '8/17/2023', 1.8),
    ('10', '8/17/2023', 2.8),
    ('11', '8/17/2023', 3.1),
    ('12', '8/17/2023', 4.3),
    ('13', '8/17/2023', 2.9),
    ('14', '8/17/2023', 4.2),
    ('15', '8/17/2023', 2.0),
    ('16', '8/17/2023', 3.6),
    ('17', '8/17/2023', 3.6),
    ('18', '8/17/2023', 3.3),
    ('19', '8/17/2023', 3.7),
    ('20', '8/17/2023', 3.8),
    ('1', '8/18/2023', 4.2),
    ('2', '8/18/2023', 4.5),
    ('3', '8/18/2023', 1.4),
    ('4', '8/18/2023', 1.2),
    ('5', '8/18/2023', 3.5),
    ('6', '8/18/2023', 4.8),
    ('7', '8/18/2023', 1.3),
    ('8', '8/18/2023', 3.5),
    ('9', '8/18/2023', 4.2),
    ('10', '8/18/2023', 4.9),
    ('11', '8/18/2023', 3.0),
    ('12', '8/18/2023', 2.5),
    ('13', '8/18/2023', 1.7),
    ('14', '8/18/2023', 4.2),
    ('15', '8/18/2023', 2.1),
    ('16', '8/18/2023', 1.7),
    ('17', '8/18/2023', 1.8),
    ('18', '8/18/2023', 2.0),
    ('19', '8/18/2023', 1.1),
    ('20', '8/18/2023', 3.9),
    ('1', '8/19/2023', 4.4),
    ('2', '8/19/2023', 4.3),
    ('3', '8/19/2023', 4.5),
    ('4', '8/19/2023', 3.8),
    ('5', '8/19/2023', 1.1),
    ('6', '8/19/2023', 2.8),
    ('7', '8/19/2023', 3.5),
    ('8', '8/19/2023', 2.3),
    ('9', '8/19/2023', 3.5),
    ('10', '8/19/2023', 1.1),
    ('11', '8/19/2023', 5.0),
    ('12', '8/19/2023', 1.4),
    ('13', '8/19/2023', 1.9),
    ('14', '8/19/2023', 3.2),
    ('15', '8/19/2023', 4.7),
    ('16', '8/19/2023', 2.1),
    ('17', '8/19/2023', 4.6),
    ('18', '8/19/2023', 4.5),
    ('19', '8/19/2023', 3.2),
    ('20', '8/19/2023', 4.4),
    ('1', '8/20/2023', 3.2),
    ('2', '8/20/2023', 3.9),
    ('3', '8/20/2023', 1.3),
    ('4', '8/20/2023', 1.5),
    ('5', '8/20/2023', 3.9),
    ('6', '8/20/2023', 2.6),
    ('7', '8/20/2023', 2.3),
    ('8', '8/20/2023', 3.5),
    ('9', '8/20/2023', 4.1),
    ('10', '8/20/2023', 2.1),
    ('11', '8/20/2023', 4.0),
    ('12', '8/20/2023', 2.5),
    ('13', '8/20/2023', 1.5),
    ('14', '8/20/2023', 4.0),
    ('15', '8/20/2023', 3.5),
    ('16', '8/20/2023', 1.7),
    ('17', '8/20/2023', 2.8),
    ('18', '8/20/2023', 3.9),
    ('19', '8/20/2023', 4.5),
    ('20', '8/20/2023', 1.6),
    ('1', '8/21/2023', 4.4),
    ('2', '8/21/2023', 4.0),
    ('3', '8/21/2023', 2.9),
    ('4', '8/21/2023', 1.8),
    ('5', '8/21/2023', 3.4),
    ('6', '8/21/2023', 3.5),
    ('7', '8/21/2023', 3.0),
    ('8', '8/21/2023', 2.1),
    ('9', '8/21/2023', 2.6),
    ('10', '8/21/2023', 4.8),
    ('11', '8/21/2023', 4.8),
    ('12', '8/21/2023', 2.0),
    ('13', '8/21/2023', 4.3),
    ('14', '8/21/2023', 1.1),
    ('15', '8/21/2023', 3.7),
    ('16', '8/21/2023', 1.7),
    ('17', '8/21/2023', 1.7),
    ('18', '8/21/2023', 4.4),
    ('19', '8/21/2023', 1.6),
    ('20', '8/21/2023', 1.2),
    ('1', '8/22/2023', 1.1),
    ('2', '8/22/2023', 2.2),
    ('3', '8/22/2023', 3.0),
    ('4', '8/22/2023', 3.1),
    ('5', '8/22/2023', 4.9),
    ('6', '8/22/2023', 3.0),
    ('7', '8/22/2023', 2.6),
    ('8', '8/22/2023', 3.3),
    ('9', '8/22/2023', 3.9),
    ('10', '8/22/2023', 2.5),
    ('11', '8/22/2023', 5.0),
    ('12', '8/22/2023', 1.7),
    ('13', '8/22/2023', 2.5),
    ('14', '8/22/2023', 4.1),
    ('15', '8/22/2023', 1.3),
    ('16', '8/22/2023', 1.8),
    ('17', '8/22/2023', 1.9),
    ('18', '8/22/2023', 1.1),
    ('19', '8/22/2023', 2.9),
    ('20', '8/22/2023', 1.6),
    ('1', '8/23/2023', 4.4),
    ('2', '8/23/2023', 4.0),
    ('3', '8/23/2023', 1.6),
    ('4', '8/23/2023', 2.6),
    ('5', '8/23/2023', 5.0),
    ('6', '8/23/2023', 1.8),
    ('7', '8/23/2023', 1.4),
    ('8', '8/23/2023', 4.8),
    ('9', '8/23/2023', 1.4),
    ('10', '8/23/2023', 2.0),
    ('11', '8/23/2023', 4.7),
    ('12', '8/23/2023', 3.6),
    ('13', '8/23/2023', 2.2),
    ('14', '8/23/2023', 4.0),
    ('15', '8/23/2023', 1.8),
    ('16', '8/23/2023', 2.6),
    ('17', '8/23/2023', 3.7),
    ('18', '8/23/2023', 1.9),
    ('19', '8/23/2023', 2.8),
    ('20', '8/23/2023', 3.8),
    ('1', '8/24/2023', 2.0),
    ('2', '8/24/2023', 4.7),
    ('3', '8/24/2023', 2.2),
    ('4', '8/24/2023', 2.1),
    ('5', '8/24/2023', 3.0),
    ('6', '8/24/2023', 1.8),
    ('7', '8/24/2023', 4.4),
    ('8', '8/24/2023', 2.2),
    ('9', '8/24/2023', 4.1),
    ('10', '8/24/2023', 3.4),
    ('11', '8/24/2023', 1.0),
    ('12', '8/24/2023', 3.5),
    ('13', '8/24/2023', 1.4),
    ('14', '8/24/2023', 2.4),
    ('15', '8/24/2023', 2.6),
    ('16', '8/24/2023', 1.4),
    ('17', '8/24/2023', 3.8),
    ('18', '8/24/2023', 4.9),
    ('19', '8/24/2023', 2.8),
    ('20', '8/24/2023', 2.1),
    ('1', '8/25/2023', 4.1),
    ('2', '8/25/2023', 3.2),
    ('3', '8/25/2023', 3.0),
    ('4', '8/25/2023', 3.8),
    ('5', '8/25/2023', 4.2),
    ('6', '8/25/2023', 3.4),
    ('7', '8/25/2023', 2.3),
    ('8', '8/25/2023', 4.9),
    ('9', '8/25/2023', 2.0),
    ('10', '8/25/2023', 4.0),
    ('11', '8/25/2023', 2.3),
    ('12', '8/25/2023', 1.1),
    ('13', '8/25/2023', 4.1),
    ('14', '8/25/2023', 3.1),
    ('15', '8/25/2023', 1.2),
    ('16', '8/25/2023', 1.9),
    ('17', '8/25/2023', 4.8),
    ('18', '8/25/2023', 3.1),
    ('19', '8/25/2023', 2.8),
    ('20', '8/25/2023', 4.5),
    ('1', '8/26/2023', 2.5),
    ('2', '8/26/2023', 1.5),
    ('3', '8/26/2023', 3.6),
    ('4', '8/26/2023', 1.9),
    ('5', '8/26/2023', 3.4),
    ('6', '8/26/2023', 4.5),
    ('7', '8/26/2023', 2.1),
    ('8', '8/26/2023', 3.1),
    ('9', '8/26/2023', 1.3),
    ('10', '8/26/2023', 3.9),
    ('11', '8/26/2023', 2.3),
    ('12', '8/26/2023', 1.0),
    ('13', '8/26/2023', 1.3),
    ('14', '8/26/2023', 3.0),
    ('15', '8/26/2023', 3.0),
    ('16', '8/26/2023', 4.1),
    ('17', '8/26/2023', 4.9),
    ('18', '8/26/2023', 3.6),
    ('19', '8/26/2023', 4.8),
    ('20', '8/26/2023', 4.8),
    ('1', '8/27/2023', 4.5),
    ('2', '8/27/2023', 2.7),
    ('3', '8/27/2023', 3.5),
    ('4', '8/27/2023', 2.6),
    ('5', '8/27/2023', 3.9),
    ('6', '8/27/2023', 4.3),
    ('7', '8/27/2023', 4.3),
    ('8', '8/27/2023', 1.6),
    ('9', '8/27/2023', 3.5),
    ('10', '8/27/2023', 2.0),
    ('11', '8/27/2023', 1.4),
    ('12', '8/27/2023', 4.4),
    ('13', '8/27/2023', 2.7),
    ('14', '8/27/2023', 5.0),
    ('15', '8/27/2023', 3.2),
    ('16', '8/27/2023', 3.7),
    ('17', '8/27/2023', 4.8),
    ('18', '8/27/2023', 2.7),
    ('19', '8/27/2023', 3.2),
    ('20', '8/27/2023', 3.8),
    ('1', '8/28/2023', 2.2),
    ('2', '8/28/2023', 2.9),
    ('3', '8/28/2023', 3.8),
    ('4', '8/28/2023', 3.6),
    ('5', '8/28/2023', 2.6),
    ('6', '8/28/2023', 1.0),
    ('7', '8/28/2023', 3.2),
    ('8', '8/28/2023', 3.2),
    ('9', '8/28/2023', 2.3),
    ('10', '8/28/2023', 2.6),
    ('11', '8/28/2023', 1.0),
    ('12', '8/28/2023', 1.8),
    ('13', '8/28/2023', 1.2),
    ('14', '8/28/2023', 3.3),
    ('15', '8/28/2023', 3.2),
    ('16', '8/28/2023', 3.7),
    ('17', '8/28/2023', 2.0),
    ('18', '8/28/2023', 1.0),
    ('19', '8/28/2023', 1.8),
    ('20', '8/28/2023', 1.3),
    ('1', '8/29/2023', 2.1),
    ('2', '8/29/2023', 1.5),
    ('3', '8/29/2023', 4.2),
    ('4', '8/29/2023', 1.4),
    ('5', '8/29/2023', 4.1),
    ('6', '8/29/2023', 4.0),
    ('7', '8/29/2023', 4.6),
    ('8', '8/29/2023', 4.6),
    ('9', '8/29/2023', 2.2),
    ('10', '8/29/2023', 2.7),
    ('11', '8/29/2023', 2.4),
    ('12', '8/29/2023', 2.9),
    ('13', '8/29/2023', 3.0),
    ('14', '8/29/2023', 1.0),
    ('15', '8/29/2023', 2.5),
    ('16', '8/29/2023', 4.2),
    ('17', '8/29/2023', 4.1),
    ('18', '8/29/2023', 2.3),
    ('19', '8/29/2023', 2.9),
    ('20', '8/29/2023', 1.1),
    ('1', '8/30/2023', 4.9),
    ('2', '8/30/2023', 3.1),
    ('3', '8/30/2023', 2.4),
    ('4', '8/30/2023', 2.1),
    ('5', '8/30/2023', 1.0),
    ('6', '8/30/2023', 2.5),
    ('7', '8/30/2023', 3.9),
    ('8', '8/30/2023', 3.3),
    ('9', '8/30/2023', 4.7),
    ('10', '8/30/2023', 1.5),
    ('11', '8/30/2023', 2.5),
    ('12', '8/30/2023', 3.9),
    ('13', '8/30/2023', 3.0),
    ('14', '8/30/2023', 4.8),
    ('15', '8/30/2023', 4.9),
    ('16', '8/30/2023', 1.4),
    ('17', '8/30/2023', 3.8),
    ('18', '8/30/2023', 2.1),
    ('19', '8/30/2023', 2.2),
    ('20', '8/30/2023', 2.1),
    ('1', '8/31/2023', 1.9),
    ('2', '8/31/2023', 2.3),
    ('3', '8/31/2023', 4.7),
    ('4', '8/31/2023', 4.5),
    ('5', '8/31/2023', 5.0),
    ('6', '8/31/2023', 4.6),
    ('7', '8/31/2023', 4.1),
    ('8', '8/31/2023', 4.2),
    ('9', '8/31/2023', 3.1),
    ('10', '8/31/2023', 2.0),
    ('11', '8/31/2023', 3.4),
    ('12', '8/31/2023', 3.2),
    ('13', '8/31/2023', 3.0),
    ('14', '8/31/2023', 4.7),
    ('15', '8/31/2023', 3.2),
    ('16', '8/31/2023', 3.8),
    ('17', '8/31/2023', 4.1),
    ('18', '8/31/2023', 4.5),
    ('19', '8/31/2023', 2.0),
    ('20', '8/31/2023', 1.1);
"""
