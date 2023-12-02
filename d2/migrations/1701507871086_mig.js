/* eslint-disable camelcase */

exports.shorthands = undefined;

exports.up = (pgm) => {
  pgm.sql(`
        CREATE TABLE hand (
            id INT,
            r INT,
            g INT,
            b INT
        );

        CREATE OR REPLACE FUNCTION get_legal_hand_sum (r_lim INT, g_lim INT, b_lim INT) RETURNS int LANGUAGE plpgsql AS $$
        BEGIN
            RETURN (
                SELECT SUM(DISTINCT id) S
                FROM hand WHERE id NOT IN (
                    SELECT id 
                    FROM hand 
                    WHERE r > r_lim OR g > g_lim OR b > b_lim
                )
            );
        END $$;

        CREATE OR REPLACE FUNCTION get_min_cubes () RETURNS int LANGUAGE plpgsql AS $$
        BEGIN
            RETURN (
                SELECT SUM(r_max * g_max * b_max) 
                FROM (
                    SELECT id, MAX(r) r_max, MAX(g) g_max, MAX(b) b_max 
                    FROM hand 
                    GROUP BY id
                ) T
            );
        END $$;
    `);
};

exports.down = (pgm) => {
  pgm.sql(`
            DROP TABLE hand;
            DROP FUNCTION get_legal_hand_sum;
            DROP FUNCTION get_min_cubes;
        `);
};
