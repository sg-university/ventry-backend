drop table if exists role cascade;
create table role
(
    id          uuid primary key,
    name        text,
    description text,
    created_at  timestamp,
    updated_at  timestamp
);

drop table if exists company cascade;
create table company
(
    id          uuid primary key,
    name        text,
    description text,
    created_at  timestamp,
    updated_at  timestamp
);

drop table if exists location cascade;
create table location
(
    id          uuid primary key,
    name        text,
    address     text,
    description text,
    created_at  timestamp,
    updated_at  timestamp
);


drop table if exists account cascade;
create table account
(
    id          uuid primary key,
    role_id     uuid,
    location_id uuid,
    name        text,
    email       text,
    password    text,
    created_at  timestamp,
    updated_at  timestamp,
    constraint account_role_role_id foreign key (role_id) references role (id) on update cascade on delete cascade,
    constraint account_location_location_id foreign key (location_id) references location (id) on update cascade on delete cascade
);


drop table if exists company_location_map cascade;
create table company_location_map
(
    id          uuid primary key,
    company_id  uuid,
    location_id uuid,
    created_at  timestamp,
    updated_at  timestamp,
    constraint company_location_map_company_company_id foreign key (company_id) references company (id) on update cascade on delete cascade,
    constraint company_location_map_location_location_id foreign key (location_id) references location (id) on update cascade on delete cascade
);

drop table if exists company_account_map cascade;
create table company_account_map
(
    id         uuid primary key,
    company_id uuid,
    account_id uuid,
    created_at timestamp,
    updated_at timestamp,
    constraint company_location_map_company_company_id foreign key (company_id) references company (id) on update cascade on delete cascade,
    constraint company_location_map_location_location_id foreign key (account_id) references account (id) on update cascade on delete cascade
);

drop table if exists item cascade;
create table item
(
    id                       uuid primary key,
    location_id              uuid,
    code                     text,
    name                     text,
    type                     text,
    description              text,
    combination_max_quantity numeric,
    combination_min_quantity numeric,
    quantity                 numeric,
    unit_name                text,
    unit_sell_price          numeric,
    unit_cost_price          numeric,
    created_at               timestamp,
    updated_at               timestamp,
    constraint item_location_location_id foreign key (location_id) references location (id) on update cascade on delete cascade
);

drop table if exists item_combination_map cascade;
create table item_combination_map
(
    id            uuid primary key,
    super_item_id uuid,
    sub_item_id   uuid,
    quantity      numeric,
    created_at    timestamp,
    updated_at    timestamp,
    constraint item_combination_map_item_super_item_id foreign key (super_item_id) references item (id) on update cascade on delete cascade,
    constraint item_combination_map_item_sub_item_id foreign key (sub_item_id) references item (id) on update cascade on delete cascade
);

drop table if exists file cascade;
create table file
(
    id          uuid primary key,
    name        text,
    description text,
    extension   text,
    content     bytea,
    created_at  timestamp,
    updated_at  timestamp
);

drop table if exists item_file_map cascade;
create table item_file_map
(
    id         uuid primary key,
    item_id    uuid,
    file_id    uuid,
    created_at timestamp,
    updated_at timestamp,
    constraint item_file_map_item_item_id foreign key (item_id) references item (id) on update cascade on delete cascade,
    constraint item_file_map_file_file_id foreign key (file_id) references file (id) on update cascade on delete cascade
);

drop table if exists inventory_control cascade;
create table inventory_control
(
    id              uuid primary key,
    account_id      uuid,
    item_id         uuid,
    quantity_before numeric,
    quantity_after  numeric,
    timestamp       timestamp,
    created_at      timestamp,
    updated_at      timestamp,
    constraint inventory_control_account_account_id foreign key (account_id) references account (id) on update cascade on delete cascade,
    constraint inventory_control_item_item_id foreign key (item_id) references item (id) on update cascade on delete cascade
);

drop table if exists transaction cascade;
create table transaction
(
    id         uuid primary key,
    account_id uuid,
    sell_price numeric,
    timestamp  timestamp,
    created_at timestamp,
    updated_at timestamp,
    constraint transaction_account_account_id foreign key (account_id) references account (id) on update cascade on delete cascade
);

drop table if exists transaction_item_map cascade;
create table transaction_item_map
(
    id             uuid primary key,
    transaction_id uuid,
    item_id        uuid,
    sell_price     numeric,
    quantity       numeric,
    created_at     timestamp,
    updated_at     timestamp,
    constraint transaction_item_map_transaction_transaction_id foreign key (transaction_id) references transaction (id) on update cascade on delete cascade,
    constraint transaction_item_map_item_item_id foreign key (item_id) references item (id) on update cascade on delete cascade
);

-- populate all table with unique data
insert into role (id, name, description, created_at, updated_at)
values ('b999ce14-2ef1-40ef-a4e3-1120d4202070', 'admin', 'admin', now(), now()),
       ('b999ce14-2ef1-40ef-a4e3-1120d4202071', 'cashier', 'cashier', now(), now());

insert into company (id, name, description, created_at, updated_at)
values ('b667e566-e9f0-4816-b91e-6fb8265bddc0', 'company0', 'first company', now(), now()),
       ('b667e566-e9f0-4816-b91e-6fb8265bddc1', 'company1', 'second company', now(), now());

insert into location (id, name, address, description, created_at, updated_at)
values ('1464b9da-6d0f-40c5-9966-de4e02e9a810', 'default', 'default', 'default', now(), now()),
       ('1464b9da-6d0f-40c5-9966-de4e02e9a811', 'default', 'default', 'default', now(), now());

insert into account (id, role_id, location_id, name, email, password, created_at, updated_at)
values ('f52151d6-0456-476a-aab8-1a0b0097a1d0', 'b999ce14-2ef1-40ef-a4e3-1120d4202070',
        '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'admin', 'admin@mail.com',
        'admin', now(), now()),
       ('f52151d6-0456-476a-aab8-1a0b0097a1d1', 'b999ce14-2ef1-40ef-a4e3-1120d4202071',
        '1464b9da-6d0f-40c5-9966-de4e02e9a811', 'cashier', 'cashier@mail.com',
        'cashier', now(), now());

insert into company_account_map (id, company_id, account_id, created_at, updated_at)
values ('5ffb5a91-d9ae-4025-ab7b-d7d07ffd1a10', 'b667e566-e9f0-4816-b91e-6fb8265bddc0',
        'f52151d6-0456-476a-aab8-1a0b0097a1d0', now(), now()),
       ('5ffb5a91-d9ae-4025-ab7b-d7d07ffd1a11', 'b667e566-e9f0-4816-b91e-6fb8265bddc1',
        'f52151d6-0456-476a-aab8-1a0b0097a1d1', now(), now());

insert into company_location_map (id, company_id, location_id, created_at, updated_at)
values ('7ec6d3fb-44ae-4c43-94a6-48e38d25c5e0', 'b667e566-e9f0-4816-b91e-6fb8265bddc0',
        '1464b9da-6d0f-40c5-9966-de4e02e9a810', now(), now()),
       ('7ec6d3fb-44ae-4c43-94a6-48e38d25c5e1', 'b667e566-e9f0-4816-b91e-6fb8265bddc1',
        '1464b9da-6d0f-40c5-9966-de4e02e9a811', now(), now());

insert into item (id, location_id, code, name, type, description, combination_max_quantity, combination_min_quantity,
                  quantity, unit_name,
                  unit_sell_price,
                  unit_cost_price, created_at, updated_at)
values ('28cacf4b-e5f5-493c-bf81-c20a2662d290', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item1', 'item1', 'goods',
        'item1', 0, 0,
        0, 'unit1', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d291', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item2', 'item2', 'goods',
        'item2', 0, 0,
        0, 'unit2', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d292', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item3', 'item3', 'goods',
        'item3', 0, 0,
        0, 'unit3', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d293', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item4', 'item4', 'goods',
        'item4', 0, 0,
        0, 'unit4', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d294', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item5', 'item5', 'goods',
        'item5', 0, 0,
        0, 'unit5', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d295', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item6', 'item6', 'goods',
        'item6', 0, 0,
        0, 'unit6', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d296', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'cuci-1kg', 'cuci-1kg',
        'services',
        'cuci-1kg', 0, 0,
        0, 'pcs', 7000, 5000, now(), now());



insert into file (id, name, description, extension, content, created_at, updated_at)
values ('f52151d6-0456-476a-aab8-1a0b0097a1d0', 'placeholder', 'placeholder', 'png',
        'data:image/png;base64,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',
        now(), now());

insert into item_file_map (id, item_id, file_id, created_at, updated_at)
values ('9db7fd77-9f3d-4772-9c94-cbce01af4bf0', '28cacf4b-e5f5-493c-bf81-c20a2662d290',
        'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        now(), now()),
       ('9db7fd77-9f3d-4772-9c94-cbce01af4bf1', '28cacf4b-e5f5-493c-bf81-c20a2662d291',
        'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        now(), now()),
       ('9db7fd77-9f3d-4772-9c94-cbce01af4bf2', '28cacf4b-e5f5-493c-bf81-c20a2662d292',
        'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        now(), now()),
       ('9db7fd77-9f3d-4772-9c94-cbce01af4bf3', '28cacf4b-e5f5-493c-bf81-c20a2662d293',
        'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        now(), now()),
       ('9db7fd77-9f3d-4772-9c94-cbce01af4bf4', '28cacf4b-e5f5-493c-bf81-c20a2662d294',
        'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        now(), now()),
       ('9db7fd77-9f3d-4772-9c94-cbce01af4bf5', '28cacf4b-e5f5-493c-bf81-c20a2662d295',
        'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        now(), now());


insert into item_combination_map (id, super_item_id, sub_item_id, quantity, created_at, updated_at)
values ('927d5249-60b5-4eb3-8fd6-f67706c113b0', '28cacf4b-e5f5-493c-bf81-c20a2662d290',
        '28cacf4b-e5f5-493c-bf81-c20a2662d292', 1, now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b1', '28cacf4b-e5f5-493c-bf81-c20a2662d290',
        '28cacf4b-e5f5-493c-bf81-c20a2662d293', 1, now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b2', '28cacf4b-e5f5-493c-bf81-c20a2662d291',
        '28cacf4b-e5f5-493c-bf81-c20a2662d293', 1, now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b3', '28cacf4b-e5f5-493c-bf81-c20a2662d292',
        '28cacf4b-e5f5-493c-bf81-c20a2662d294', 1, now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b4', '28cacf4b-e5f5-493c-bf81-c20a2662d293',
        '28cacf4b-e5f5-493c-bf81-c20a2662d294', 1, now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b5', '28cacf4b-e5f5-493c-bf81-c20a2662d293',
        '28cacf4b-e5f5-493c-bf81-c20a2662d295', 1, now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b6', '28cacf4b-e5f5-493c-bf81-c20a2662d290',
        '28cacf4b-e5f5-493c-bf81-c20a2662d294', 1, now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b7', '28cacf4b-e5f5-493c-bf81-c20a2662d291',
        '28cacf4b-e5f5-493c-bf81-c20a2662d295', 1, now(), now());

insert into inventory_control (id, account_id, item_id, quantity_before, quantity_after, timestamp, created_at,
                               updated_at)
values ('927d5249-60b5-4eb3-8fd6-f67706c113b0', 'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d290',
        0, 1, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b1', 'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d291',
        0, 1, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b2', 'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d292',
        0, 1, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b3', 'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d293',
        0, 1, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b4', 'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d294',
        0, 1, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b5', 'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d295',
        0, 1, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b6', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d290',
        1, 0, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b7', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d291',
        1, 0, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b8', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d292',
        1, 0, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c113b9', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d293',
        1, 0, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c11310', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d294',
        1, 0, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c11311', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d295',
        1, 0, now(), now(), now());

insert into transaction (id, account_id, sell_price, timestamp, created_at, updated_at)
values ('20354d7a-e4fe-47af-8ff6-187bca92f3f0', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f1', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f2', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f3', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f4', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f5', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f6', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f7', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 867000, '2021/03/1'::timestamp,
        '2021/03/1'::timestamp, '2021/03/1'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f8', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 816000, '2021/03/2'::timestamp,
        '2021/03/2'::timestamp, '2021/03/2'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f9', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 670000, '2021/03/3'::timestamp,
        '2021/03/3'::timestamp, '2021/03/3'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f310', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 393000, '2021/03/4'::timestamp,
        '2021/03/4'::timestamp, '2021/03/4'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f311', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 695000, '2021/03/5'::timestamp,
        '2021/03/5'::timestamp, '2021/03/5'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f312', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 692000, '2021/03/6'::timestamp,
        '2021/03/6'::timestamp, '2021/03/6'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f313', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 618000, '2021/03/7'::timestamp,
        '2021/03/7'::timestamp, '2021/03/7'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f314', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 578000, '2021/03/8'::timestamp,
        '2021/03/8'::timestamp, '2021/03/8'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f315', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 441500, '2021/03/9'::timestamp,
        '2021/03/9'::timestamp, '2021/03/9'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f316', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 333000, '2021/03/10'::timestamp,
        '2021/03/10'::timestamp, '2021/03/10'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f317', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 744000, '2021/03/11'::timestamp,
        '2021/03/11'::timestamp, '2021/03/11'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f318', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 638000, '2021/03/12'::timestamp,
        '2021/03/12'::timestamp, '2021/03/12'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f319', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 905000, '2021/03/13'::timestamp,
        '2021/03/13'::timestamp, '2021/03/13'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f320', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 604000, '2021/03/15'::timestamp,
        '2021/03/15'::timestamp, '2021/03/15'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f321', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 530000, '2021/03/16'::timestamp,
        '2021/03/16'::timestamp, '2021/03/16'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f322', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 499000, '2021/03/17'::timestamp,
        '2021/03/17'::timestamp, '2021/03/17'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f323', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 568000, '2021/03/18'::timestamp,
        '2021/03/18'::timestamp, '2021/03/18'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f324', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 642000, '2021/03/19'::timestamp,
        '2021/03/19'::timestamp, '2021/03/19'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f325', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 460000, '2021/03/20'::timestamp,
        '2021/03/20'::timestamp, '2021/03/20'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f326', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 729000, '2021/03/21'::timestamp,
        '2021/03/21'::timestamp, '2021/03/21'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f327', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 514000, '2021/03/22'::timestamp,
        '2021/03/22'::timestamp, '2021/03/22'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f328', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 584500, '2021/03/23'::timestamp,
        '2021/03/23'::timestamp, '2021/03/23'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f329', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 509000, '2021/03/24'::timestamp,
        '2021/03/24'::timestamp, '2021/03/24'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f330', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 483000, '2021/03/25'::timestamp,
        '2021/03/25'::timestamp, '2021/03/25'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f331', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 645000, '2021/03/26'::timestamp,
        '2021/03/26'::timestamp, '2021/03/26'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f332', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 567000, '2021/03/27'::timestamp,
        '2021/03/27'::timestamp, '2021/03/27'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f333', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 529000, '2021/03/28'::timestamp,
        '2021/03/28'::timestamp, '2021/03/28'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f334', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 860000, '2021/03/29'::timestamp,
        '2021/03/29'::timestamp, '2021/03/29'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f335', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 915000, '2021/03/30'::timestamp,
        '2021/03/30'::timestamp, '2021/03/30'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f336', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 363000, '2021/03/31'::timestamp,
        '2021/03/31'::timestamp, '2021/03/31'::timestamp),
       ('20354d7a-e4fe-47af-8ff6-187bca92f337', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 403500, '2021/04/1'::timestamp,
        '2021/04/1'::timestamp, '2021/04/1'::timestamp);

insert into transaction_item_map (id, transaction_id, item_id, quantity, sell_price, created_at, updated_at)
values ('4636decc-3828-45a2-b350-fa2281f87ef0', '20354d7a-e4fe-47af-8ff6-187bca92f3f0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d290', 1, 1200, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef1', '20354d7a-e4fe-47af-8ff6-187bca92f3f1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d291', 1, 1200, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef2', '20354d7a-e4fe-47af-8ff6-187bca92f3f2',
        '28cacf4b-e5f5-493c-bf81-c20a2662d292', 1, 1200, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef3', '20354d7a-e4fe-47af-8ff6-187bca92f3f3',
        '28cacf4b-e5f5-493c-bf81-c20a2662d293', 1, 1200, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef4', '20354d7a-e4fe-47af-8ff6-187bca92f3f4',
        '28cacf4b-e5f5-493c-bf81-c20a2662d294', 1, 1200, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef5', '20354d7a-e4fe-47af-8ff6-187bca92f3f5',
        '28cacf4b-e5f5-493c-bf81-c20a2662d295', 1, 1200, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef6', '20354d7a-e4fe-47af-8ff6-187bca92f3f7',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 121.7, 867000, '2021/03/1'::timestamp, '2021/03/1'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87ef7', '20354d7a-e4fe-47af-8ff6-187bca92f3f8',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 98, 816000, '2021/03/2'::timestamp, '2021/03/2'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87ef8', '20354d7a-e4fe-47af-8ff6-187bca92f3f9',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 85.9, 670000, '2021/03/3'::timestamp, '2021/03/3'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87ef9', '20354d7a-e4fe-47af-8ff6-187bca92f310',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 58.7, 393000, '2021/03/4'::timestamp, '2021/03/4'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e10', '20354d7a-e4fe-47af-8ff6-187bca92f311',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 101.1, 695000, '2021/03/5'::timestamp, '2021/03/5'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e11', '20354d7a-e4fe-47af-8ff6-187bca92f312',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 96.5, 692000, '2021/03/6'::timestamp, '2021/03/6'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e12', '20354d7a-e4fe-47af-8ff6-187bca92f313',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 89.5, 618000, '2021/03/7'::timestamp, '2021/03/7'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e13', '20354d7a-e4fe-47af-8ff6-187bca92f314',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 81.3, 578000, '2021/03/8'::timestamp, '2021/03/8'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e14', '20354d7a-e4fe-47af-8ff6-187bca92f315',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 30.7, 441500, '2021/03/9'::timestamp, '2021/03/9'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e15', '20354d7a-e4fe-47af-8ff6-187bca92f316',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 44.1, 333000, '2021/03/10'::timestamp, '2021/03/10'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e16', '20354d7a-e4fe-47af-8ff6-187bca92f317',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 84.1, 744000, '2021/03/11'::timestamp, '2021/03/11'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e17', '20354d7a-e4fe-47af-8ff6-187bca92f318',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 97.9, 638000, '2021/03/12'::timestamp, '2021/03/12'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e18', '20354d7a-e4fe-47af-8ff6-187bca92f319',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 119.6, 905000, '2021/03/13'::timestamp, '2021/03/13'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e19', '20354d7a-e4fe-47af-8ff6-187bca92f320',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 68.6, 604000, '2021/03/15'::timestamp, '2021/03/15'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e20', '20354d7a-e4fe-47af-8ff6-187bca92f321',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 69.6, 530000, '2021/03/16'::timestamp, '2021/03/16'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e21', '20354d7a-e4fe-47af-8ff6-187bca92f322',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 62.8, 499000, '2021/03/17'::timestamp, '2021/03/17'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e22', '20354d7a-e4fe-47af-8ff6-187bca92f323',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 82.5, 568000, '2021/03/18'::timestamp, '2021/03/18'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e23', '20354d7a-e4fe-47af-8ff6-187bca92f324',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 80.3, 642000, '2021/03/19'::timestamp, '2021/03/19'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e24', '20354d7a-e4fe-47af-8ff6-187bca92f325',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 59.8, 460000, '2021/03/20'::timestamp, '2021/03/20'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e25', '20354d7a-e4fe-47af-8ff6-187bca92f326',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 98.4, 729000, '2021/03/21'::timestamp, '2021/03/21'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e26', '20354d7a-e4fe-47af-8ff6-187bca92f327',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 77.7, 514000, '2021/03/22'::timestamp, '2021/03/22'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e27', '20354d7a-e4fe-47af-8ff6-187bca92f328',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 83, 584500, '2021/03/23'::timestamp, '2021/03/23'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e28', '20354d7a-e4fe-47af-8ff6-187bca92f329',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 67.9, 509000, '2021/03/24'::timestamp, '2021/03/24'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e29', '20354d7a-e4fe-47af-8ff6-187bca92f330',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 55.1, 483000, '2021/03/25'::timestamp, '2021/03/25'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e30', '20354d7a-e4fe-47af-8ff6-187bca92f331',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 103.7, 645000, '2021/03/26'::timestamp, '2021/03/26'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e31', '20354d7a-e4fe-47af-8ff6-187bca92f332',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 76.7, 567000, '2021/03/27'::timestamp, '2021/03/27'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e32', '20354d7a-e4fe-47af-8ff6-187bca92f333',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 74.2, 529000, '2021/03/28'::timestamp, '2021/03/28'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e33', '20354d7a-e4fe-47af-8ff6-187bca92f334',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 134.6, 860000, '2021/03/29'::timestamp, '2021/03/29'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e34', '20354d7a-e4fe-47af-8ff6-187bca92f335',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 114.2, 915000, '2021/03/30'::timestamp, '2021/03/30'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e35', '20354d7a-e4fe-47af-8ff6-187bca92f336',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 46.5, 363000, '2021/03/31'::timestamp, '2021/03/31'::timestamp),
       ('4636decc-3828-45a2-b350-fa2281f87e36', '20354d7a-e4fe-47af-8ff6-187bca92f337',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 65.3, 403500, '2021/04/1'::timestamp, '2021/04/1'::timestamp);

--


select *
from item_combination_map;


select t.id, t.timestamp
from transaction t;

select tim.item_id,
       sum(tim.quantity),
       (select t2.timestamp from transaction t2 where t2.id = tim.transaction_id) as timestamp
from transaction_item_map tim
where tim.item_id = '28cacf4b-e5f5-493c-bf81-c20a2662d296'
group by tim.item_id, tim.transaction_id
order by timestamp asc;


select *
from account;