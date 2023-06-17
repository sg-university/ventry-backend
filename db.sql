drop table if exists role cascade;
create table role
(
    id          uuid primary key,
    name        text,
    description text,
    created_at  timestamptz,
    updated_at  timestamptz
);

drop table if exists company cascade;
create table company
(
    id          uuid primary key,
    name        text,
    description text,
    address     text,
    created_at  timestamptz,
    updated_at  timestamptz
);

drop table if exists location cascade;
create table location
(
    id          uuid primary key,
    company_id  uuid,
    name        text,
    address     text,
    description text,
    created_at  timestamptz,
    updated_at  timestamptz,
    constraint location_company_company_id foreign key (company_id) references company (id) on update cascade on delete cascade
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
    created_at  timestamptz,
    updated_at  timestamptz,
    constraint account_role_role_id foreign key (role_id) references role (id) on update cascade on delete cascade,
    constraint account_location_location_id foreign key (location_id) references location (id) on update cascade on delete cascade
);

drop table if exists item cascade;
create table item
(
    id              uuid primary key,
    location_id     uuid,
    code            text,
    name            text,
    type            text,
    description     text,
    quantity        numeric,
    unit_name       text,
    unit_sell_price numeric,
    unit_cost_price numeric,
    image           bytea,
    created_at      timestamptz,
    updated_at      timestamptz,
    constraint item_location_location_id foreign key (location_id) references location (id) on update cascade on delete cascade
);

drop table if exists item_bundle_map cascade;
create table item_bundle_map
(
    id            uuid primary key,
    super_item_id uuid,
    sub_item_id   uuid,
    quantity      numeric,
    created_at    timestamptz,
    updated_at    timestamptz,
    constraint item_bundle_map_item_super_item_id foreign key (super_item_id) references item (id) on update cascade on delete cascade,
    constraint item_bundle_map_item_sub_item_id foreign key (sub_item_id) references item (id) on update cascade on delete cascade
);

drop table if exists inventory_control cascade;
create table inventory_control
(
    id              uuid primary key,
    account_id      uuid,
    item_id         uuid,
    quantity_before numeric,
    quantity_after  numeric,
    timestamp       timestamptz,
    created_at      timestamptz,
    updated_at      timestamptz,
    constraint inventory_control_account_account_id foreign key (account_id) references account (id) on update cascade on delete cascade,
    constraint inventory_control_item_item_id foreign key (item_id) references item (id) on update cascade on delete cascade
);

drop table if exists transaction cascade;
create table transaction
(
    id         uuid primary key,
    account_id uuid,
    sell_price numeric,
    timestamp  timestamptz,
    created_at timestamptz,
    updated_at timestamptz,
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
    created_at     timestamptz,
    updated_at     timestamptz,
    constraint transaction_item_map_transaction_transaction_id foreign key (transaction_id) references transaction (id) on update cascade on delete cascade,
    constraint transaction_item_map_item_item_id foreign key (item_id) references item (id) on update cascade on delete cascade
);

-- populate all table with unique data
insert into role (id, name, description, created_at, updated_at)
values ('b999ce14-2ef1-40ef-a4e3-1120d4202070', 'admin', 'admin', now(), now()),
       ('b999ce14-2ef1-40ef-a4e3-1120d4202071', 'cashier', 'cashier', now(), now());

insert into company (id, name, description, address, created_at, updated_at)
values ('b667e566-e9f0-4816-b91e-6fb8265bddc0', 'name0', 'description0', 'address0', now(), now()),
       ('b667e566-e9f0-4816-b91e-6fb8265bddc1', 'name1', 'description1', 'address1', now(), now());

insert into location (id, company_id, name, description, address, created_at, updated_at)
values ('1464b9da-6d0f-40c5-9966-de4e02e9a810', 'b667e566-e9f0-4816-b91e-6fb8265bddc0', 'name0', 'description0',
        'address0', now(), now()),
       ('1464b9da-6d0f-40c5-9966-de4e02e9a811', 'b667e566-e9f0-4816-b91e-6fb8265bddc1', 'name1', 'description1',
        'address1', now(), now());

insert into account (id, role_id, location_id, name, email, password, created_at, updated_at)
values ('f52151d6-0456-476a-aab8-1a0b0097a1d0', 'b999ce14-2ef1-40ef-a4e3-1120d4202070',
        '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'admin', 'admin@mail.com',
        'admin', now(), now()),
       ('f52151d6-0456-476a-aab8-1a0b0097a1d1', 'b999ce14-2ef1-40ef-a4e3-1120d4202071',
        '1464b9da-6d0f-40c5-9966-de4e02e9a811', 'cashier', 'cashier@mail.com',
        'cashier', now(), now());

insert into item (id, location_id,
                  code, name,
                  type, description,
                  quantity, unit_name,
                  unit_sell_price, unit_cost_price,
                  image,
                  created_at, updated_at)
values ('28cacf4b-e5f5-493c-bf81-c20a2662d290', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item0', 'item0', 'goods',
        'item1',
        0, 'unit1', 1200, 1000, null, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d291', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item1', 'item1', 'goods',
        'item2',
        0, 'unit2', 1200, 1000, null, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d292', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item2', 'item2', 'goods',
        'item3',
        0, 'unit3', 1200, 1000, null, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d293', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item3', 'item3', 'goods',
        'item4',
        0, 'unit4', 1200, 1000, null, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d294', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item4', 'item4', 'goods',
        'item5',
        0, 'unit5', 1200, 1000, null, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d295', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item5', 'item5', 'goods',
        'item6',
        0, 'unit6', 1200, 1000, null, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d296', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'cuci-1kg', 'cuci-1kg',
        'services',
        'cuci-1kg',
        0, 'pcs', 7000, 5000, null, now(), now());


insert into item_bundle_map (id, super_item_id, sub_item_id, quantity, created_at, updated_at)
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
        1, 0, now(), now(), now()),
       ('927d5249-60b5-4eb3-8fd6-f67706c11312', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296',
        0, 100, '2021/03/1'::timestamptz, '2021/03/1'::timestamptz, '2021/03/1'::timestamptz),
       ('927d5249-60b5-4eb3-8fd6-f67706c11313', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296',
        100, 50, '2021/03/2'::timestamptz, '2021/03/2'::timestamptz, '2021/03/2'::timestamptz),
       ('927d5249-60b5-4eb3-8fd6-f67706c11314', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296',
        50, 25, '2021/03/3'::timestamptz, '2021/03/3'::timestamptz, '2021/03/3'::timestamptz),
       ('927d5249-60b5-4eb3-8fd6-f67706c11315', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296',
        25, 75, '2021/03/4'::timestamptz, '2021/03/4'::timestamptz, '2021/03/4'::timestamptz),
       ('927d5249-60b5-4eb3-8fd6-f67706c11316', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296',
        75, 50, '2021/03/5'::timestamptz, '2021/03/5'::timestamptz, '2021/03/5'::timestamptz),
       ('927d5249-60b5-4eb3-8fd6-f67706c11317', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296',
        50, 25, '2021/03/6'::timestamptz, '2021/03/6'::timestamptz, '2021/03/6'::timestamptz),
       ('927d5249-60b5-4eb3-8fd6-f67706c11318', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296',
        25, 75, '2021/03/7'::timestamptz, '2021/03/7'::timestamptz, '2021/03/7'::timestamptz);

insert into transaction (id, account_id, sell_price, timestamp, created_at, updated_at)
values ('20354d7a-e4fe-47af-8ff6-187bca92f3f0', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f1', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f2', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f3', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f4', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f5', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f6', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 1200, now(), now(), now()),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f7', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 867000,
        '2021/03/1'::timestamptz,
        '2021/03/1'::timestamptz, '2021/03/1'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f8', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 816000,
        '2021/03/2'::timestamptz,
        '2021/03/2'::timestamptz, '2021/03/2'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f9', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 670000,
        '2021/03/3'::timestamptz,
        '2021/03/3'::timestamptz, '2021/03/3'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f310', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 393000,
        '2021/03/4'::timestamptz,
        '2021/03/4'::timestamptz, '2021/03/4'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f311', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 695000,
        '2021/03/5'::timestamptz,
        '2021/03/5'::timestamptz, '2021/03/5'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f312', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 692000,
        '2021/03/6'::timestamptz,
        '2021/03/6'::timestamptz, '2021/03/6'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f313', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 618000,
        '2021/03/7'::timestamptz,
        '2021/03/7'::timestamptz, '2021/03/7'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f314', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 578000,
        '2021/03/8'::timestamptz,
        '2021/03/8'::timestamptz, '2021/03/8'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f315', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 441500,
        '2021/03/9'::timestamptz,
        '2021/03/9'::timestamptz, '2021/03/9'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f316', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 333000,
        '2021/03/10'::timestamptz,
        '2021/03/10'::timestamptz, '2021/03/10'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f317', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 744000,
        '2021/03/11'::timestamptz,
        '2021/03/11'::timestamptz, '2021/03/11'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f318', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 638000,
        '2021/03/12'::timestamptz,
        '2021/03/12'::timestamptz, '2021/03/12'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f319', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 905000,
        '2021/03/13'::timestamptz,
        '2021/03/13'::timestamptz, '2021/03/13'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f320', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 604000,
        '2021/03/15'::timestamptz,
        '2021/03/15'::timestamptz, '2021/03/15'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f321', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 530000,
        '2021/03/16'::timestamptz,
        '2021/03/16'::timestamptz, '2021/03/16'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f322', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 499000,
        '2021/03/17'::timestamptz,
        '2021/03/17'::timestamptz, '2021/03/17'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f323', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 568000,
        '2021/03/18'::timestamptz,
        '2021/03/18'::timestamptz, '2021/03/18'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f324', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 642000,
        '2021/03/19'::timestamptz,
        '2021/03/19'::timestamptz, '2021/03/19'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f325', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 460000,
        '2021/03/20'::timestamptz,
        '2021/03/20'::timestamptz, '2021/03/20'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f326', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 729000,
        '2021/03/21'::timestamptz,
        '2021/03/21'::timestamptz, '2021/03/21'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f327', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 514000,
        '2021/03/22'::timestamptz,
        '2021/03/22'::timestamptz, '2021/03/22'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f328', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 584500,
        '2021/03/23'::timestamptz,
        '2021/03/23'::timestamptz, '2021/03/23'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f329', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 509000,
        '2021/03/24'::timestamptz,
        '2021/03/24'::timestamptz, '2021/03/24'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f330', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 483000,
        '2021/03/25'::timestamptz,
        '2021/03/25'::timestamptz, '2021/03/25'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f331', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 645000,
        '2021/03/26'::timestamptz,
        '2021/03/26'::timestamptz, '2021/03/26'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f332', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 567000,
        '2021/03/27'::timestamptz,
        '2021/03/27'::timestamptz, '2021/03/27'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f333', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 529000,
        '2021/03/28'::timestamptz,
        '2021/03/28'::timestamptz, '2021/03/28'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f334', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 860000,
        '2021/03/29'::timestamptz,
        '2021/03/29'::timestamptz, '2021/03/29'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f335', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 915000,
        '2021/03/30'::timestamptz,
        '2021/03/30'::timestamptz, '2021/03/30'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f336', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 363000,
        '2021/03/31'::timestamptz,
        '2021/03/31'::timestamptz, '2021/03/31'::timestamptz),
       ('20354d7a-e4fe-47af-8ff6-187bca92f337', 'f52151d6-0456-476a-aab8-1a0b0097a1d0', 403500,
        '2021/04/1'::timestamptz,
        '2021/04/1'::timestamptz, '2021/04/1'::timestamptz);

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
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 121.7, 867000, '2021/03/1'::timestamptz, '2021/03/1'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87ef7', '20354d7a-e4fe-47af-8ff6-187bca92f3f8',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 98, 816000, '2021/03/2'::timestamptz, '2021/03/2'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87ef8', '20354d7a-e4fe-47af-8ff6-187bca92f3f9',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 85.9, 670000, '2021/03/3'::timestamptz, '2021/03/3'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87ef9', '20354d7a-e4fe-47af-8ff6-187bca92f310',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 58.7, 393000, '2021/03/4'::timestamptz, '2021/03/4'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e10', '20354d7a-e4fe-47af-8ff6-187bca92f311',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 101.1, 695000, '2021/03/5'::timestamptz, '2021/03/5'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e11', '20354d7a-e4fe-47af-8ff6-187bca92f312',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 96.5, 692000, '2021/03/6'::timestamptz, '2021/03/6'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e12', '20354d7a-e4fe-47af-8ff6-187bca92f313',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 89.5, 618000, '2021/03/7'::timestamptz, '2021/03/7'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e13', '20354d7a-e4fe-47af-8ff6-187bca92f314',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 81.3, 578000, '2021/03/8'::timestamptz, '2021/03/8'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e14', '20354d7a-e4fe-47af-8ff6-187bca92f315',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 30.7, 441500, '2021/03/9'::timestamptz, '2021/03/9'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e15', '20354d7a-e4fe-47af-8ff6-187bca92f316',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 44.1, 333000, '2021/03/10'::timestamptz, '2021/03/10'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e16', '20354d7a-e4fe-47af-8ff6-187bca92f317',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 84.1, 744000, '2021/03/11'::timestamptz, '2021/03/11'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e17', '20354d7a-e4fe-47af-8ff6-187bca92f318',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 97.9, 638000, '2021/03/12'::timestamptz, '2021/03/12'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e18', '20354d7a-e4fe-47af-8ff6-187bca92f319',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 119.6, 905000, '2021/03/13'::timestamptz, '2021/03/13'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e19', '20354d7a-e4fe-47af-8ff6-187bca92f320',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 68.6, 604000, '2021/03/15'::timestamptz, '2021/03/15'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e20', '20354d7a-e4fe-47af-8ff6-187bca92f321',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 69.6, 530000, '2021/03/16'::timestamptz, '2021/03/16'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e21', '20354d7a-e4fe-47af-8ff6-187bca92f322',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 62.8, 499000, '2021/03/17'::timestamptz, '2021/03/17'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e22', '20354d7a-e4fe-47af-8ff6-187bca92f323',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 82.5, 568000, '2021/03/18'::timestamptz, '2021/03/18'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e23', '20354d7a-e4fe-47af-8ff6-187bca92f324',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 80.3, 642000, '2021/03/19'::timestamptz, '2021/03/19'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e24', '20354d7a-e4fe-47af-8ff6-187bca92f325',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 59.8, 460000, '2021/03/20'::timestamptz, '2021/03/20'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e25', '20354d7a-e4fe-47af-8ff6-187bca92f326',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 98.4, 729000, '2021/03/21'::timestamptz, '2021/03/21'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e26', '20354d7a-e4fe-47af-8ff6-187bca92f327',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 77.7, 514000, '2021/03/22'::timestamptz, '2021/03/22'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e27', '20354d7a-e4fe-47af-8ff6-187bca92f328',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 83, 584500, '2021/03/23'::timestamptz, '2021/03/23'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e28', '20354d7a-e4fe-47af-8ff6-187bca92f329',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 67.9, 509000, '2021/03/24'::timestamptz, '2021/03/24'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e29', '20354d7a-e4fe-47af-8ff6-187bca92f330',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 55.1, 483000, '2021/03/25'::timestamptz, '2021/03/25'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e30', '20354d7a-e4fe-47af-8ff6-187bca92f331',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 103.7, 645000, '2021/03/26'::timestamptz, '2021/03/26'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e31', '20354d7a-e4fe-47af-8ff6-187bca92f332',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 76.7, 567000, '2021/03/27'::timestamptz, '2021/03/27'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e32', '20354d7a-e4fe-47af-8ff6-187bca92f333',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 74.2, 529000, '2021/03/28'::timestamptz, '2021/03/28'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e33', '20354d7a-e4fe-47af-8ff6-187bca92f334',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 134.6, 860000, '2021/03/29'::timestamptz, '2021/03/29'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e34', '20354d7a-e4fe-47af-8ff6-187bca92f335',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 114.2, 915000, '2021/03/30'::timestamptz, '2021/03/30'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e35', '20354d7a-e4fe-47af-8ff6-187bca92f336',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 46.5, 363000, '2021/03/31'::timestamptz, '2021/03/31'::timestamptz),
       ('4636decc-3828-45a2-b350-fa2281f87e36', '20354d7a-e4fe-47af-8ff6-187bca92f337',
        '28cacf4b-e5f5-493c-bf81-c20a2662d296', 65.3, 403500, '2021/04/1'::timestamptz, '2021/04/1'::timestamptz);

--


select *
from item_bundle_map;

select tim.item_id,
       sum(tim.quantity),
       (select t.timestamp from transaction t where t.id = tim.transaction_id) as timestamp
from transaction_item_map tim
where tim.item_id = '28cacf4b-e5f5-493c-bf81-c20a2662d296'
group by tim.item_id, tim.transaction_id
order by timestamp asc;


select *
from company c
         inner join location l on l.company_id = c.id
         inner join account a on a.location_id = l.id
where c.id in ('b667e566-e9f0-4816-b91e-6fb8265bddc1', 'b667e566-e9f0-4816-b91e-6fb8265bddc0');


select *
from item i
         inner join account a on a.location_id = i.location_id
where a.location_id = '1464b9da-6d0f-40c5-9966-de4e02e9a810';

SELECT a.*
from account a
WHERE 'b667e566-e9f0-4816-b91e-6fb8265bddc0' in (SELECT c.id
                                                 FROM account a
                                                          INNER JOIN location l on l.id = a.location_id
                                                          INNER JOIN company c on c.id = l.company_id);

-- select all account in different location with same company id
select a.*
from account a
where a.location_id in (select l.id
                        from location l
                        where l.company_id = 'b667e566-e9f0-4816-b91e-6fb8265bddc1');

select *
from transaction
         inner join transaction_item_map tim on transaction.id = tim.transaction_id;

select *
from inventory_control;

select *
from location l
         inner join company c on l.company_id = c.id