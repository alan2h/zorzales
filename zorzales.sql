--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: articulos_articulo; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.articulos_articulo (
    fecha_compra timestamp with time zone,
    id integer NOT NULL,
    codigo_barra character varying(900),
    descripcion character varying(800) NOT NULL,
    precio_compra numeric(8,2),
    stock integer,
    stock_minimo integer,
    imagen character varying(100),
    alicuota_iva numeric(12,2),
    marca_id integer,
    rubro_id integer,
    precio_venta numeric(8,2)
);


ALTER TABLE public.articulos_articulo OWNER TO abeck;

--
-- Name: articulos_articulo_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.articulos_articulo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.articulos_articulo_id_seq OWNER TO abeck;

--
-- Name: articulos_articulo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.articulos_articulo_id_seq OWNED BY public.articulos_articulo.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO abeck;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO abeck;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO abeck;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO abeck;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO abeck;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO abeck;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO abeck;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO abeck;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO abeck;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO abeck;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO abeck;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO abeck;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: clientes_cliente; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.clientes_cliente (
    persona_ptr_id integer NOT NULL,
    baja boolean NOT NULL,
    fecha_baja date,
    motivo character varying(600),
    foto character varying(100),
    email character varying(300),
    telefono character varying(300)
);


ALTER TABLE public.clientes_cliente OWNER TO abeck;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO abeck;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO abeck;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO abeck;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO abeck;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO abeck;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO abeck;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO abeck;

--
-- Name: marcas_marca; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.marcas_marca (
    id integer NOT NULL,
    descripcion character varying(800) NOT NULL
);


ALTER TABLE public.marcas_marca OWNER TO abeck;

--
-- Name: marcas_marca_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.marcas_marca_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.marcas_marca_id_seq OWNER TO abeck;

--
-- Name: marcas_marca_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.marcas_marca_id_seq OWNED BY public.marcas_marca.id;


--
-- Name: personas_persona; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.personas_persona (
    id integer NOT NULL,
    nombre character varying(3000) NOT NULL,
    apellido character varying(3000) NOT NULL,
    fecha_nacimiento date
);


ALTER TABLE public.personas_persona OWNER TO abeck;

--
-- Name: personas_persona_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.personas_persona_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.personas_persona_id_seq OWNER TO abeck;

--
-- Name: personas_persona_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.personas_persona_id_seq OWNED BY public.personas_persona.id;


--
-- Name: rubros_rubro; Type: TABLE; Schema: public; Owner: abeck
--

CREATE TABLE public.rubros_rubro (
    id integer NOT NULL,
    descripcion character varying(800) NOT NULL
);


ALTER TABLE public.rubros_rubro OWNER TO abeck;

--
-- Name: rubros_rubro_id_seq; Type: SEQUENCE; Schema: public; Owner: abeck
--

CREATE SEQUENCE public.rubros_rubro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rubros_rubro_id_seq OWNER TO abeck;

--
-- Name: rubros_rubro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: abeck
--

ALTER SEQUENCE public.rubros_rubro_id_seq OWNED BY public.rubros_rubro.id;


--
-- Name: articulos_articulo id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.articulos_articulo ALTER COLUMN id SET DEFAULT nextval('public.articulos_articulo_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: marcas_marca id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.marcas_marca ALTER COLUMN id SET DEFAULT nextval('public.marcas_marca_id_seq'::regclass);


--
-- Name: personas_persona id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.personas_persona ALTER COLUMN id SET DEFAULT nextval('public.personas_persona_id_seq'::regclass);


--
-- Name: rubros_rubro id; Type: DEFAULT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.rubros_rubro ALTER COLUMN id SET DEFAULT nextval('public.rubros_rubro_id_seq'::regclass);


--
-- Data for Name: articulos_articulo; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.articulos_articulo (fecha_compra, id, codigo_barra, descripcion, precio_compra, stock, stock_minimo, imagen, alicuota_iva, marca_id, rubro_id, precio_venta) FROM stdin;
\N	1		asdasds	\N	\N	\N		\N	\N	\N	\N
\N	2		asdasds	\N	\N	\N		\N	\N	\N	\N
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add persona	7	add_persona
26	Can change persona	7	change_persona
27	Can delete persona	7	delete_persona
28	Can view persona	7	view_persona
29	Can add cliente	8	add_cliente
30	Can change cliente	8	change_cliente
31	Can delete cliente	8	delete_cliente
32	Can view cliente	8	view_cliente
33	Can add Rubro	9	add_rubro
34	Can change Rubro	9	change_rubro
35	Can delete Rubro	9	delete_rubro
36	Can view Rubro	9	view_rubro
37	Can add Marca	10	add_marca
38	Can change Marca	10	change_marca
39	Can delete Marca	10	delete_marca
40	Can view Marca	10	view_marca
41	Can add Artículos	11	add_articulo
42	Can change Artículos	11	change_articulo
43	Can delete Artículos	11	delete_articulo
44	Can view Artículos	11	view_articulo
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$180000$CGSKkbiouZcv$dWRv/EiZPKnjMRq6TX26U0Y7tKmppdNqP21c/qVKAM4=	2020-02-04 12:15:03.569933-03	t	admin				t	t	2020-01-28 14:29:20.889124-03
1	pbkdf2_sha256$180000$IHNGGZf0VXMH$j4121Zew3NOmLYrk3Mr+pGrDBee7h/QSyPdyZlGxWxI=	2020-02-20 13:39:11.231353-03	t	abeck				t	t	2020-01-06 11:48:06.652419-03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: clientes_cliente; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.clientes_cliente (persona_ptr_id, baja, fecha_baja, motivo, foto, email, telefono) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-01-06 12:40:34.759789-03	1	asd, asd	1	[{"added": {}}]	8	1
2	2020-02-14 12:02:57.233005-03	1	Los toros	1	[{"added": {}}]	10	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	personas	persona
8	clientes	cliente
9	rubros	rubro
10	marcas	marca
11	articulos	articulo
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-01-06 11:47:46.579235-03
2	auth	0001_initial	2020-01-06 11:47:46.631826-03
3	admin	0001_initial	2020-01-06 11:47:46.684132-03
4	admin	0002_logentry_remove_auto_add	2020-01-06 11:47:46.702324-03
5	admin	0003_logentry_add_action_flag_choices	2020-01-06 11:47:46.713706-03
6	contenttypes	0002_remove_content_type_name	2020-01-06 11:47:46.734586-03
7	auth	0002_alter_permission_name_max_length	2020-01-06 11:47:46.740817-03
8	auth	0003_alter_user_email_max_length	2020-01-06 11:47:46.75231-03
9	auth	0004_alter_user_username_opts	2020-01-06 11:47:46.761007-03
10	auth	0005_alter_user_last_login_null	2020-01-06 11:47:46.770181-03
11	auth	0006_require_contenttypes_0002	2020-01-06 11:47:46.77245-03
12	auth	0007_alter_validators_add_error_messages	2020-01-06 11:47:46.780666-03
13	auth	0008_alter_user_username_max_length	2020-01-06 11:47:46.794275-03
14	auth	0009_alter_user_last_name_max_length	2020-01-06 11:47:46.803189-03
15	auth	0010_alter_group_name_max_length	2020-01-06 11:47:46.811813-03
16	auth	0011_update_proxy_permissions	2020-01-06 11:47:46.821582-03
17	personas	0001_initial	2020-01-06 11:47:46.83011-03
18	clientes	0001_initial	2020-01-06 11:47:46.838526-03
19	sessions	0001_initial	2020-01-06 11:47:46.846453-03
20	clientes	0002_cliente_foto	2020-01-06 12:13:34.705294-03
21	clientes	0003_auto_20200204_1645	2020-02-04 16:45:24.133805-03
22	rubros	0001_initial	2020-02-14 11:58:17.674005-03
23	marcas	0001_initial	2020-02-14 12:02:42.947545-03
24	articulos	0001_initial	2020-02-14 16:06:13.849121-03
25	articulos	0002_articulo_precio_venta	2020-02-14 16:08:49.57241-03
26	articulos	0003_auto_20200217_1610	2020-02-17 16:10:26.016148-03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
o7vhirwwjgi79wegvmkjrb2jlclp94me	MTJkYzNkODIwMDc2YjZkMzk5NWE2OGEyZmJhYTQ3NTRlY2MyNDUzMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNGE5YzllNzFjYTNlMjEyMGU5NmI3MjUyMzIzMDIzY2JiZTJkYWUyIn0=	2020-01-20 12:23:24.766528-03
hqxlclch1hgr725v3mdg9bon5n3hqtir	MGU3NTk0ODdlMWYwYjk0M2JiZDhlZTliMDQyMWVhZGI2ZjAxOGFkOTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwM2Q1NTQzNjE4YjFkYmU1NGM0NTJjMTQwZTc3NTZiYTU3NjI1ZTJiIn0=	2020-02-11 14:30:10.431645-03
qil68ssrn81ohsyqwbf9xl4qzoy0nclv	MTJkYzNkODIwMDc2YjZkMzk5NWE2OGEyZmJhYTQ3NTRlY2MyNDUzMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNGE5YzllNzFjYTNlMjEyMGU5NmI3MjUyMzIzMDIzY2JiZTJkYWUyIn0=	2020-02-28 16:05:48.394824-03
jauuaq0ckljm0086r2gs1s3errttwihs	MTJkYzNkODIwMDc2YjZkMzk5NWE2OGEyZmJhYTQ3NTRlY2MyNDUzMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNGE5YzllNzFjYTNlMjEyMGU5NmI3MjUyMzIzMDIzY2JiZTJkYWUyIn0=	2020-03-05 13:39:11.281653-03
\.


--
-- Data for Name: marcas_marca; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.marcas_marca (id, descripcion) FROM stdin;
36	asdasdsd
1	Los toroszzzzzz
\.


--
-- Data for Name: personas_persona; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.personas_persona (id, nombre, apellido, fecha_nacimiento) FROM stdin;
\.


--
-- Data for Name: rubros_rubro; Type: TABLE DATA; Schema: public; Owner: abeck
--

COPY public.rubros_rubro (id, descripcion) FROM stdin;
\.


--
-- Name: articulos_articulo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.articulos_articulo_id_seq', 2, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 34, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: marcas_marca_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.marcas_marca_id_seq', 36, true);


--
-- Name: personas_persona_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.personas_persona_id_seq', 8, true);


--
-- Name: rubros_rubro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: abeck
--

SELECT pg_catalog.setval('public.rubros_rubro_id_seq', 1, false);


--
-- Name: articulos_articulo articulos_articulo_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.articulos_articulo
    ADD CONSTRAINT articulos_articulo_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: clientes_cliente clientes_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.clientes_cliente
    ADD CONSTRAINT clientes_cliente_pkey PRIMARY KEY (persona_ptr_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: marcas_marca marcas_marca_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.marcas_marca
    ADD CONSTRAINT marcas_marca_pkey PRIMARY KEY (id);


--
-- Name: personas_persona personas_persona_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.personas_persona
    ADD CONSTRAINT personas_persona_pkey PRIMARY KEY (id);


--
-- Name: rubros_rubro rubros_rubro_pkey; Type: CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.rubros_rubro
    ADD CONSTRAINT rubros_rubro_pkey PRIMARY KEY (id);


--
-- Name: articulos_articulo_marca_id_c3c2458c; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX articulos_articulo_marca_id_c3c2458c ON public.articulos_articulo USING btree (marca_id);


--
-- Name: articulos_articulo_rubro_id_eafb36aa; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX articulos_articulo_rubro_id_eafb36aa ON public.articulos_articulo USING btree (rubro_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: abeck
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: articulos_articulo articulos_articulo_marca_id_c3c2458c_fk_marcas_marca_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.articulos_articulo
    ADD CONSTRAINT articulos_articulo_marca_id_c3c2458c_fk_marcas_marca_id FOREIGN KEY (marca_id) REFERENCES public.marcas_marca(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: articulos_articulo articulos_articulo_rubro_id_eafb36aa_fk_rubros_rubro_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.articulos_articulo
    ADD CONSTRAINT articulos_articulo_rubro_id_eafb36aa_fk_rubros_rubro_id FOREIGN KEY (rubro_id) REFERENCES public.rubros_rubro(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: clientes_cliente clientes_cliente_persona_ptr_id_3c1f9c00_fk_personas_persona_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.clientes_cliente
    ADD CONSTRAINT clientes_cliente_persona_ptr_id_3c1f9c00_fk_personas_persona_id FOREIGN KEY (persona_ptr_id) REFERENCES public.personas_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: abeck
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

