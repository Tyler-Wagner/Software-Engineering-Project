CREATE TABLE ipInfo (
    from_IpADD VARCHAR(15) NOT NULL PRIMARY KEY,
    dest_IpADD VARCHAR(15) NOT NULL,
    port INTEGER NOT NULL,
    protocol VARCHAR(100) NOT NULL,
    allow BOOLEAN
);
