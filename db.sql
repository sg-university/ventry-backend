drop table if exists role cascade;
create table role
(
    id          uuid primary key,
    name        text,
    description text,
    created_at  timestamp,
    updated_at  timestamp
);

drop table if exists account cascade;
create table account
(
    id         uuid primary key,
    role_id    uuid,
    name       text,
    email      text,
    password   text,
    created_at timestamp,
    updated_at timestamp,
    constraint account_role_role_id foreign key (role_id) references role (id) on update cascade on delete cascade
);

drop table if exists permission cascade;
create table permission
(
    id          uuid primary key,
    name        text,
    description text,
    created_at  timestamp,
    updated_at  timestamp
);

drop table if exists account_permission_map cascade;
create table account_permission_map
(
    id            uuid primary key,
    account_id    uuid,
    permission_id uuid,
    created_at    timestamp,
    updated_at    timestamp,
    constraint account_permission_map_account_account_id foreign key (account_id) references account (id) on update cascade on delete cascade,
    constraint account_permission_map_permission_permission_id foreign key (permission_id) references permission (id) on update cascade on delete cascade
);

drop table if exists item cascade;
create table item
(
    id                       uuid primary key,
    permission_id            uuid,
    code                     text,
    name                     text,
    description              text,
    combination_max_quantity numeric,
    combination_min_quantity numeric,
    quantity                 numeric,
    unit_name                text,
    unit_sell_price          numeric,
    unit_cost_price          numeric,
    created_at               timestamp,
    updated_at               timestamp,
    constraint item_permission_permission_id foreign key (permission_id) references permission (id) on update cascade on delete cascade
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

insert into account (id, role_id, name, email, password, created_at, updated_at)
values ('f52151d6-0456-476a-aab8-1a0b0097a1d0', 'b999ce14-2ef1-40ef-a4e3-1120d4202070', 'admin', 'admin@mail.com',
        'admin', now(), now()),
       ('f52151d6-0456-476a-aab8-1a0b0097a1d1', 'b999ce14-2ef1-40ef-a4e3-1120d4202071', 'cashier', 'cashier@mail.com',
        'cashier', now(), now());

insert into permission (id, name, description, created_at, updated_at)
values ('1464b9da-6d0f-40c5-9966-de4e02e9a810', 'default', 'default', now(), now()),
       ('1464b9da-6d0f-40c5-9966-de4e02e9a811', 'default', 'default', now(), now());

insert into account_permission_map (id, account_id, permission_id, created_at, updated_at)
values ('ca6c809c-fdf1-488c-8c60-f91f3732f2c0', 'f52151d6-0456-476a-aab8-1a0b0097a1d0',
        '1464b9da-6d0f-40c5-9966-de4e02e9a810', now(), now()),
       ('ca6c809c-fdf1-488c-8c60-f91f3732f2c1', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '1464b9da-6d0f-40c5-9966-de4e02e9a811', now(), now()),
       ('ca6c809c-fdf1-488c-8c60-f91f3732f2c2', 'f52151d6-0456-476a-aab8-1a0b0097a1d1',
        '1464b9da-6d0f-40c5-9966-de4e02e9a810', now(), now());

insert into item (id, permission_id, code, name, description, combination_max_quantity, combination_min_quantity,
                  quantity, unit_name,
                  unit_sell_price,
                  unit_cost_price, created_at, updated_at)
values ('28cacf4b-e5f5-493c-bf81-c20a2662d290', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item1', 'item1', 'item1', 0, 0,
        0,
        'unit1', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d291', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item2', 'item2', 'item2', 0, 0,
        0,
        'unit2', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d292', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item3', 'item3', 'item3', 0, 0,
        0,
        'unit3', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d293', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item4', 'item4', 'item4', 0, 0,
        0,
        'unit4', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d294', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item5', 'item5', 'item5', 0, 0,
        0,
        'unit5', 1200, 1000, now(), now()),
       ('28cacf4b-e5f5-493c-bf81-c20a2662d295', '1464b9da-6d0f-40c5-9966-de4e02e9a810', 'item6', 'item6', 'item6', 0, 0,
        0,
        'unit6', 1200, 1000, now(), now());

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
       ('20354d7a-e4fe-47af-8ff6-187bca92f3f5', 'f52151d6-0456-476a-aab8-1a0b0097a1d1', 1200, now(), now(), now());

insert into transaction_item_map (id, transaction_id, item_id, sell_price, quantity, created_at, updated_at)
values ('4636decc-3828-45a2-b350-fa2281f87ef0', '20354d7a-e4fe-47af-8ff6-187bca92f3f0',
        '28cacf4b-e5f5-493c-bf81-c20a2662d290', 1200, 1, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef1', '20354d7a-e4fe-47af-8ff6-187bca92f3f1',
        '28cacf4b-e5f5-493c-bf81-c20a2662d291', 1200, 1, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef2', '20354d7a-e4fe-47af-8ff6-187bca92f3f2',
        '28cacf4b-e5f5-493c-bf81-c20a2662d292', 1200, 1, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef3', '20354d7a-e4fe-47af-8ff6-187bca92f3f3',
        '28cacf4b-e5f5-493c-bf81-c20a2662d293', 1200, 1, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef4', '20354d7a-e4fe-47af-8ff6-187bca92f3f4',
        '28cacf4b-e5f5-493c-bf81-c20a2662d294', 1200, 1, now(), now()),
       ('4636decc-3828-45a2-b350-fa2281f87ef5', '20354d7a-e4fe-47af-8ff6-187bca92f3f5',
        '28cacf4b-e5f5-493c-bf81-c20a2662d295', 1200, 1, now(), now());


select *
from item_combination_map;
