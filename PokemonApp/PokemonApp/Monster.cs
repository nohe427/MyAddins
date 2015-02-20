using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PokemonApp
{
    class Monster
    {
        /// <summary>
        /// The level of the monster
        /// </summary>
        private int _level;

        public int Level
        {
            get { return _level; }
            set { _level = value; }
        }
        /// <summary>
        /// The type of monster that this is
        /// </summary>
        private string _type;

        public string Type
        {
            get { return _type; }
            set { _type = value; }
        }
        /// <summary>
        /// The name of the monster
        /// </summary>
        private string _name;

        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }
        /// <summary>
        /// The skills the monster has
        /// </summary>
        private List<Skills> _skills;

        internal List<Skills> Skills
        {
            get { return _skills; }
            set { _skills = value; }
        }
        /// <summary>
        /// The health the monster has
        /// </summary>
        private int _health;

        public int Health
        {
            get { return _health; }
            set { _health = value; }
        }
        /// <summary>
        /// The amount of xp the monster currently has
        /// </summary>
        private int _xp;

        public int Xp
        {
            get { return _xp; }
            set { _xp = value; }
        }
        /// <summary>
        /// The monsters strength
        /// </summary>
        private int _attack;

        public int Attack
        {
            get { return _attack; }
            set { _attack = value; }
        }
        /// <summary>
        /// The speed of the monster
        /// </summary>
        private int _speed;

        public int Speed
        {
            get { return _speed; }
            set { _speed = value; }
        }
        /// <summary>
        /// The special attack attribute
        /// </summary>
        private int _specialAttack;

        public int SpecialAttack
        {
            get { return _specialAttack; }
            set { _specialAttack = value; }
        }
        /// <summary>
        /// The special defense attribute
        /// </summary>
        private int _specialDefense;

        public int SpecialDefense
        {
            get { return _specialDefense; }
            set { _specialDefense = value; }
        }
        /// <summary>
        /// The defense attribute
        /// </summary>
        private int _defense;

        public int Defense
        {
            get { return _defense; }
            set { _defense = value; }
        }

        /// <summary>
        /// Whether or not the monster is poisoned
        /// </summary>
        private bool _poisoned;

        public bool Poisoned
        {
            get { return _poisoned; }
            set { _poisoned = value; }
        }

        /// <summary>
        /// The next level at which the pokemon evolves
        /// </summary>
        private int _nextEvolution;

        public int NextEvolution
        {
            get { return _nextEvolution; }
            set { _nextEvolution = value; }
        }
        /// <summary>
        /// Amount of XP required to level up
        /// </summary>
        private int _xpToNextLevel;

        public int XpToNextLevel
        {
            get { return _xpToNextLevel; }
            set { _xpToNextLevel = value; }
        }
        /// <summary>
        /// Image of the monster
        /// </summary>
        private System.Drawing.Image _image;

        public System.Drawing.Image Image
        {
            get { return _image; }
            set { _image = value; }
        }

        /// <summary>
        /// Maximum amount of health
        /// </summary>
        private int _maxHealth;

        public int MaxHealth
        {
            get { return _maxHealth; }
            set { _maxHealth = value; }
        }
    }
}
