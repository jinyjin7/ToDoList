from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, name, gender, bio, age, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            bio=bio,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender, bio, age, password=None):
        user = self.create_user(
            email=email,
            name=name,
            gender=gender,
            bio=bio,
            age=age,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    # name, gender, age, 
    name = models.CharField(max_length=30)
    gender = (
        ('남자','남자'),
        ('여자','여자'),
    )
    gender = models.CharField(choices=gender,max_length=2)
    age = models.CharField(max_length=3)
    bio = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","age","gender","bio"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
