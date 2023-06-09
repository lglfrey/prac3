set ansi_nulls on
go
set ansi_padding on
go
set quoted_identifier on
go

create database [Restaurant]
go 

use [Restaurant]
go

create table [Lasagna]
(
	[ID_Lasagna] [int] not null identity(1,1) primary key,
	[Cost_Lasagna] [int] not null
)
go

insert into [Lasagna] ([Cost_Lasagna]) values
(200)
go

select * from [Lasagna]
go

create table [Admin]
(
	[ID_Admin] [int] not null identity(1,1) primary key,
	[Phone_Admin] [VARCHAR] (15) not null unique check ([Phone_Admin] like ('+[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
	[Password_Admin] [VARCHAR] (50) not null,
	[Balance_Admin] [int] not null default(10000)
)
go

insert into [Admin] ([Phone_Admin], [Password_Admin], [Balance_Admin]) values
('+79851341035', 'admin', 10000)
go

select * from [Admin]
go

create table [Type_Ingridient]
(
	[ID_Type] [int] not null identity(1,1) primary key,
	[Name_Type] [VARCHAR] (50) not null unique
)
go

insert into [Type_Ingridient] ([Name_Type]) values
('����� �������'),
('����'),
('���'),
('�������'),
('�������� �����'),
('�����'),
('����'),
('������'),
('���')
go

select * from [Type_Ingridient]
go

create table [Loyality]
(
	[ID_Loyality] [int] not null identity(1,1) primary key,
	[Name_Loyality] [VARCHAR] (50) not null unique,
	[Discount] [float] not null
)
go

insert into [Loyality] ([Name_Loyality], [Discount]) values
('None', 0),
('Bronze', 0.15),
('Silver', 0.25),
('Gold', 0.35)
go

select * from [Loyality]
go

create table [User]
(
	[ID_User] [int] not null identity(1,1) primary key,
	[Loyality_ID] [int] not null references [Loyality] (ID_Loyality) on delete cascade,
	[Phone_User] [VARCHAR](15) not null unique check ([Phone_User] like ('+[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
	[Password_User] [VARCHAR](50) not null,
	[Balance_User] [int] not null default(10000)
)
go

insert into [User] ([Loyality_ID], [Phone_User], [Password_User], [Balance_User]) values
(1, '+79267247181', 'user', 10000),
(1, '+79013650372', 'user1', 10000)
go

select * from [User]
go

create table [Ingridient]
(
	[ID_Ingridient] [int] not null identity(1,1) primary key,
	[Type_ID] [int] not null references [Type_Ingridient] (ID_Type) on delete cascade,
	[Name_Ingridient] [VARCHAR](50) not null unique,
	[Cost_Ingridient] [int] not null,
	[Count_Ingridient] [int] not null default(100)
)
go

insert into [Ingridient] ([Type_ID], [Name_Ingridient], [Cost_Ingridient], [Count_Ingridient]) values
(1, '��������', 10, 10),
(1, '���������� ���������', 15, 100),
(1, '���������� �����������', 15, 100),
(2, '�������', 20, 100),
(2, '�������', 20, 100),
(2, '���������', 20, 100),
(3, '�����', 10, 100),
(3, '��������', 10, 100),
(3, '�����', 10, 100),
(4, '�������', 50, 100),
(4, '��������', 50, 100),
(4, '������', 50, 100),
(5, '�������', 50, 100),
(5, '���������', 50, 100),
(6, '���������', 20, 100),
(6, '������������', 20, 100),
(6, '���������', 20, 100),
(7, '���������', 30, 100),
(7, '������', 30, 100),
(7, '����������', 45, 100),
(8, '������������', 50, 100),
(8, '��������', 50, 100),
(8, '������', 50, 100),
(9, '�������', 100, 100),
(9, '������', 100, 100),
(9, '����������', 100, 100)
go

select * from [Ingridient]
go

create table [Supply]
(
	[ID_Supply] [int] not null identity(1,1) primary key,
	[Admin_ID] [int] not null references [Admin] (ID_Admin) on delete cascade,
	[Ingridient_ID] [int] not null references [Ingridient] (ID_Ingridient) on delete cascade,
	[Count_Supply] [int] not null,
	[Cost_Supply] [int] not null,
	[Sum_Supply] [int] not null
)
go

insert into [Supply] ([Admin_ID], [Ingridient_ID], [Count_Supply], [Cost_Supply], [Sum_Supply]) values
(1, 1, 20, 20, 400)
go

select * from [Supply]
go

create table [Lasagna_Ingridient]
(
	[ID_Lasagna_Ingridient] [int] not null identity(1,1) primary key,
	[Lasagna_ID] [int] not null references [Lasagna] (ID_Lasagna) on delete cascade,
	[Ingridient_ID] [int] not null references [Ingridient] (ID_Ingridient) on delete cascade
)
go

insert into [Lasagna_Ingridient] ([Lasagna_ID], [Ingridient_ID]) values
(1, 1),
(1, 3),
(1, 5),
(1, 7),
(1, 9),
(1, 11),
(1, 13)
go

select * from [Lasagna_Ingridient]
go

create table [Cheque]
(
	[ID_Cheque] [int] not null identity(1,1) primary key,
	[User_ID] [int] not null references [User] (ID_User) on delete cascade,
	[Count_Lasagna] [int] not null,
	[Cost_Lasagna] [int] not null,
	[Sum_Order] [int] not null,
	[Time_Order] [datetime] not null,
	[Ear] [bit] not null
)
go

insert into [Cheque] ([User_ID], [Count_Lasagna], [Cost_Lasagna], [Sum_Order], [Time_Order], [Ear]) values
(1, 1, 290, 290, SYSDATETIME(), 0)
go

select * from [Cheque]
go

create table [Cheque_Lasagna]
(
	[ID_Cheque_Lasagna] [int] not null identity(1,1) primary key,
	[Cheque_ID] [int] not null references [Cheque] (ID_Cheque) on delete cascade,
	[Cheque_Lasagna_ID] [int] not null references [Lasagna] (ID_Lasagna) on delete cascade
)
go

insert into [Cheque_Lasagna] ([Cheque_ID], [Cheque_Lasagna_ID]) values
(1,1)
go

select * from [Cheque_Lasagna]
go