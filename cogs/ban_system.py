from optparse import Option
<<<<<<< HEAD
from pickletools import int4
from pydoc import cli
from typing_extensions import Required
=======
>>>>>>> 984c1e1be8064fba178704eb04a7259ddc01c88a
from async_timeout import timeout
import nextcord
from nextcord import Guild, Member, member
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
from nextcord import Interaction, SlashOption, ChannelType
<<<<<<< HEAD
from datetime import datetime, timedelta

=======
from datetime import datetime
>>>>>>> 984c1e1be8064fba178704eb04a7259ddc01c88a

testServerId = 907299002586894367

class ban_system(commands.Cog):
    def __init__(self, client):
        self.client = client


    @nextcord.slash_command(name="kick",description="Use this command to kick members!",guild_ids=[testServerId])
    async def kick(self, interaction: Interaction,member: Member = nextcord.SlashOption(required=True),time:int=nextcord.SlashOption(required=True),reason:str=nextcord.SlashOption(required=True)):
        if interaction.user.guild_permissions.kick_members:
            if member.name != interaction.user.name:
                await member.kick(reason=reason)
                await interaction.response.send_message(f'User {member.mention} has been kicked')
            else:
                embed_error_action=nextcord.Embed(
                    title="Error",
                    colour= nextcord.Colour.red(),
                    description="You cannot do this action to yourself!"
                )
                    
                embed_error_action.timestamp = datetime.now()
                
                await interaction.response.send_message(embed=embed_error_action)   
        else:
            embed_error_perms=nextcord.Embed(
                title="Error",
                colour= nextcord.Colour.red(),
                description="You do not have the required permissions!"
            )
                    
            embed_error_perms.timestamp = datetime.now()
            
            await interaction.response.send_message(embed=embed_error_perms)
    
    @nextcord.slash_command(name="ban",description="Use this command to ban members!",guild_ids=[testServerId])
    async def ban(self, interaction: Interaction,member: Member = nextcord.SlashOption(description="Please select a member", required=True),reason=nextcord.SlashOption(description="Please type a valid reason", required=True)):
        if interaction.user.guild_permissions.ban_members:
            if member.name != interaction.user.name:
                
                await member.ban(reason=reason)
                await interaction.response.send_message(f'User {member.mention} has been banned')
            else:
                embed_error_action=nextcord.Embed(
                    title="Error",
                    colour= nextcord.Colour.red(),
                    description="You cannot do this action to yourself!"
                )
                    
                embed_error_action.timestamp = datetime.now()
                
                await interaction.response.send_message(embed=embed_error_action)   
        else:
            embed_error_perms=nextcord.Embed(
                title="Error",
                colour= nextcord.Colour.red(),
                description="You do not have the required permissions!"
            )
                    
            embed_error_perms.timestamp = datetime.now()
            
            await interaction.response.send_message(embed=embed_error_perms)


    @nextcord.slash_command(name="timeout", description="Put a user in timeout",guild_ids=[testServerId])
    
    async def timeout(self, interaction:Interaction, member: Member=nextcord.SlashOption(required=True), days:int=nextcord.SlashOption(required=False),hours:int=nextcord.SlashOption(required=False),minutes:int=nextcord.SlashOption(required=False),seconds:int=nextcord.SlashOption(required=False), reason:str=nextcord.SlashOption(required=False)):
        if interaction.user.guild_permissions.kick_members:
            if member.name != interaction.user.name:
                
                if days == None:
                    days = 0
                if hours == None:
                    hours = 0
                if minutes == None:
                    minutes = 0
                if seconds == None:
                    seconds = 0
    
    
                duration = timedelta(days=days, hours=hours, minutes=minutes,seconds=seconds)
                await member.timeout(timeout=duration)
                embed_success_timeout=nextcord.Embed(
                    title="Timeout Success",
                    colour= nextcord.Colour.green(),
                    description=f"{member.mention} has been successfully put in timeout by {interaction.user.mention} for {days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)"
                )
                        
                embed_success_timeout.timestamp = datetime.now()
                
                await interaction.response.send_message(embed=embed_success_timeout)
            else:
                embed_error_action=nextcord.Embed(
                    title="Error",
                    colour= nextcord.Colour.red(),
                    description="You cannot do this action to yourself!"
                )
                    
                embed_error_action.timestamp = datetime.now()
                
                await interaction.response.send_message(embed=embed_error_action)   
        else:
            embed_error_perms=nextcord.Embed(
                title="Error",
                colour= nextcord.Colour.red(),
                description="You do not have the required permissions!"
            )
                    
            embed_error_perms.timestamp = datetime.now()
            
            await interaction.response.send_message(embed=embed_error_perms)
<<<<<<< HEAD
        
    @nextcord.slash_command(name="remove-timeout",description="Remove a users timeout",guild_ids=[testServerId])
    async def remove_timeout(self, interaction:Interaction, user: Member=nextcord.SlashOption(required=True)):
        if interaction.user.guild_permissions.kick_members:
            
            duration = timedelta(days=0, hours=0, minutes=0,seconds=0)
            await user.timeout(duration)
            embed_success_remove_timeout=nextcord.Embed(
                title="Timeout Success",
                colour= nextcord.Colour.green(),
                description=f"{user.mention} has been successfully unmuted by {interaction.user.mention}"
            )
                        
            embed_success_remove_timeout.timestamp = datetime.now()
                
            await interaction.response.send_message(embed=embed_success_remove_timeout)
=======
>>>>>>> 984c1e1be8064fba178704eb04a7259ddc01c88a

        else:
            embed_error_perms=nextcord.Embed(
                title="Error",
                colour= nextcord.Colour.red(),
                description="You do not have the required permissions!"
            )
                    
            embed_error_perms.timestamp = datetime.now()
            
            await interaction.response.send_message(embed=embed_error_perms)   
    
    @nextcord.slash_command(name="unban",description="Use this command to unban members!",guild_ids=[testServerId])
    async def unban(self, interaction: Interaction,member:str= nextcord.SlashOption(description="Please type the members username", required=True)):
        if interaction.user.guild_permissions.ban_members:
            banned_users = await interaction.guild.bans()
            member_name, member_hash_code = member.split("#")
        
            for ban_entry in banned_users:
                user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_hash_code):
                await interaction.guild.unban(user)
                await interaction.response.send_message(f'User {user.mention} has been unbanned!')
        else:
            embed_error_perms=nextcord.Embed(
                title="Error",
                colour= nextcord.Colour.red(),
                description="You do not have the required permissions!"
            )
                    
            embed_error_perms.timestamp = datetime.now()
            
            await interaction.response.send_message(embed=embed_error_perms)
            

def setup(client):
    client.add_cog(ban_system(client))